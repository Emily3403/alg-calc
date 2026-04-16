#!/usr/bin/env bash

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"

source "$SCRIPT_DIR/venv/bin/activate"

dmypy run alg-calc tests
flake8 alg-calc tests
