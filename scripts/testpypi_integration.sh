#!/usr/bin/env bash
#
# -*- bash -*-
# shellcheck shell=bash
#
# Test PyPI Integration Testing Script
#
# This script tests the DEPLOYED package from test-pypi (not local code).
# It creates an isolated environment to ensure we're testing the actual
# published artifact.
#
# Usage:
#   ./scripts/testpypi_integration.sh <VERSION> [PYTHON] [DJANGO_VERSION] [PORT]
#
# Examples:
#   ./scripts/testpypi_integration.sh 6.0.0.123.20260130.83438
#   ./scripts/testpypi_integration.sh 6.0.0.123.20260130.83438 python3.12
#   ./scripts/testpypi_integration.sh 6.0.0.123.20260130.83438 python3.12 5.2
#   ./scripts/testpypi_integration.sh 6.0.0.123.20260130.83438 python3.12 5.2 8021
#

set -euo pipefail

PREFIX="[Test PyPI Integration]"

# Parse arguments
VERSION="${1:-}"
PYTHON="${2:-python3}"
DJANGO_VERSION="${3:-}"
DJANGO_TEST_PORT="${4:-${DJANGO_TEST_PORT:-8000}}"

if [[ -z "${VERSION}" ]]; then
    echo "${PREFIX} ERROR: VERSION argument is required"
    echo "Usage: ${0} <VERSION> [PYTHON] [DJANGO_VERSION] [PORT]"
    exit 1
fi

echo "${PREFIX} Testing django-letsencrypt version: ${VERSION}"
echo "${PREFIX} Using Python: ${PYTHON}"
echo "${PREFIX} Using port: ${DJANGO_TEST_PORT}"
[[ -n "${DJANGO_VERSION}" ]] && echo "${PREFIX} Django version: ${DJANGO_VERSION}"

# Store the original project directory (where tests live)
PROJECT_DIR="$(pwd)"

# Create a temporary working directory
WORK_DIR=$(mktemp -d)
echo "${PREFIX} Created temp directory: ${WORK_DIR}"

# Cleanup function
cleanup() {
    echo "${PREFIX} Cleaning up..."

    # Kill server if running
    if [[ -n "${SERVER_PID:-}" ]]; then
        kill "${SERVER_PID}" 2>/dev/null || true
        echo "${PREFIX} Killed server PID ${SERVER_PID}"
    fi

    # Remove temp directory
    rm -rf "${WORK_DIR}"
    echo "${PREFIX} Removed temp directory"
}
trap cleanup EXIT

# Copy example_project to temp directory
cp -r "${PROJECT_DIR}/example_project" "${WORK_DIR}/example_project"
rm -f "${WORK_DIR}/example_project/db.sqlite3"
echo "${PREFIX} Copied example_project to temp directory (fresh database)"

# Create isolated virtual environment
${PYTHON} -m venv "${WORK_DIR}/.venv"
echo "${PREFIX} Created virtual environment"

# Activate the virtual environment
# shellcheck disable=SC1091
source "${WORK_DIR}/.venv/bin/activate"
echo "${PREFIX} Activated virtual environment"

# Upgrade pip
pip install --upgrade pip --quiet

# Install Django if specific version requested
if [[ -n "${DJANGO_VERSION}" ]]; then
    echo "${PREFIX} Installing Django ${DJANGO_VERSION}..."
    pip install "Django>=${DJANGO_VERSION},<$((${DJANGO_VERSION%%.*} + 1))" --quiet
fi

# Install django-letsencrypt from test-pypi
echo "${PREFIX} Installing django-letsencrypt==${VERSION} from test-pypi..."
pip install \
    --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple/ \
    "django-letsencrypt==${VERSION}"

# Show what was installed
echo "${PREFIX} Installed packages:"
pip list | grep -E "(django|letsencrypt|pytz)"

# Navigate to the example project
cd "${WORK_DIR}/example_project"

# Run migrations
echo "${PREFIX} Running migrations..."
python manage.py migrate --settings=example_project.settings

# Create example data
echo "${PREFIX} Creating example data..."
python ./create_example_data.py

# Start the server in background
echo "${PREFIX} Starting Django development server on port ${DJANGO_TEST_PORT}..."
python manage.py runserver "127.0.0.1:${DJANGO_TEST_PORT}" --settings=example_project.settings > /dev/null 2>&1 &
SERVER_PID=$!
echo "${PREFIX} Server PID is ${SERVER_PID}"

# Wait for server to boot with retry logic
echo "${PREFIX} Waiting for server to start..."
MAX_RETRIES=30
RETRY_COUNT=0
while ! curl -s "http://127.0.0.1:${DJANGO_TEST_PORT}/" > /dev/null 2>&1; do
    RETRY_COUNT=$((RETRY_COUNT + 1))
    if [[ ${RETRY_COUNT} -ge ${MAX_RETRIES} ]]; then
        echo "${PREFIX} ERROR: Server failed to start after ${MAX_RETRIES} attempts"
        exit 1
    fi
    if ! kill -0 "${SERVER_PID}" 2>/dev/null; then
        echo "${PREFIX} ERROR: Server process died"
        exit 1
    fi
    sleep 0.5
done
echo "${PREFIX} Server is ready (took ${RETRY_COUNT} attempts)"

# Run integration tests (using pytest from the temp venv)
echo "${PREFIX} Running integration tests..."
cd "${PROJECT_DIR}"

# Install pytest in the temp venv if needed
pip install pytest --quiet

# Run the integration tests
DJANGO_TEST_PORT="${DJANGO_TEST_PORT}" pytest -v ./tests/integration/

echo "${PREFIX} Integration tests passed!"
