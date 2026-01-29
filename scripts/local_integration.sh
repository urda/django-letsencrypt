#!/usr/bin/env bash
#
# -*- bash -*-
# shellcheck shell=bash

set -euo pipefail

PREFIX="[Local Integration]"

pushd ./example_project/

make setup-project

make run-project > /dev/null 2>&1 & SERVER_PID=${!} ; echo "Server PID is ... ${SERVER_PID}"

popd

echo "${PREFIX} sleeping as server boots..." && sleep 2

uv run pytest -v ./tests/integration/

kill ${SERVER_PID}
echo "${PREFIX} killed server via PID ${SERVER_PID}"

rm example_project/db.sqlite3
echo "${PREFIX} removed local test database"
