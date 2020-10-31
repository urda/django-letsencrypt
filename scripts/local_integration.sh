#!/usr/bin/env bash
#
# -*- bash -*-
# shellcheck shell=bash

set -euo pipefail

PREFIX="[Local Integration]"

pushd ./example_project/

echo "${PREFIX} Removed local library link."
rm ./letsencrypt

pip install django-letsencrypt==4.0.0

make setup-project

make run-project > /dev/null 2>&1 & SERVER_PID=${!} ; echo "Server PID is ... ${SERVER_PID}"

popd

echo "${PREFIX} sleeping as server boots..." && sleep 2

pytest -v ./tests/integration/

kill ${SERVER_PID}
echo "${PREFIX} killed server via PID ${SERVER_PID}"

rm example_project/db.sqlite3
echo "${PREFIX} removed local test database"

git restore example_project/letsencrypt
echo "${PREFIX} restored local library link"
