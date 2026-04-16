#!/usr/bin/env bash

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"

source "$SCRIPT_DIR/venv/bin/activate"

dmypy run alg_calc tests
flake8 alg_calc tests
