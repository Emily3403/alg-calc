from __future__ import annotations

import os
import platform
import sys
from datetime import datetime
from pathlib import Path
from typing import Callable, NoReturn

error_text = "\033[1;91mError:\033[0m"
warning_text = "\033[1;33mWarning:\033[0m"

# Ripped from https://github.com/Emily3403/LeagueClashAnalyzer
def error_exit(code: int, reason: str) -> NoReturn:
    print(f"{error_text} {reason}", flush=True)
    os._exit(code)


# The `--force` argument exists to provide the user to _explicitly_ confirm their choice and understand why the application might be crashing.
if sys.version_info <= (3, 10) and "--force" not in sys.argv:
    error_exit(
        1,
        f"Python version >=3.10 was expected, but {platform.python_version()} was encountered.\n"
        "Please update your python to version 3.10 or higher in order to run this app!\n\n"
        f"If you are feeling lucky, you may bypass this check by running `league_clash_analyzer --force`"
    )

# --- General settings ---

# state
working_dir_location = Path(os.path.dirname(__file__), "resources")
config_file_location = working_dir_location / "config.json"


# A constant to detect if you are on Linux.
is_linux = platform.system() == "Linux"

# A constant to detect if you are on macOS.
is_macos = platform.system() == "Darwin"

# A constant to detect if you are on Windows.
is_windows = platform.system() == "Windows"

# -/- General settings ---


# --- Plotting settings ---

plot_directory_location = "plots"
current_plot_directory_location = os.path.join(plot_directory_location, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# -/- Plotting settings ---


# --- Database Configuration ---

sqlite_database_name = "alg-calc.db"

database_mariadb_username = "testuser"
database_mariadb_password = "testpw"
database_mariadb_database_name = "alg-calc"
database_use_mariadb = False
database_verbose_sql = False

_sqlalchemy_database_url: Callable[[str], str] = lambda it: f"sqlite:///{it}"
sqlalchemy_sqlite_database_url = _sqlalchemy_database_url(os.path.join(working_dir_location, sqlite_database_name))

if database_use_mariadb:
    if (host := os.getenv("MYSQL_HOST")) is not None:
        _sqlalchemy_database_url = lambda \
                database_name: f"mariadb+mariadbconnector://{database_mariadb_username}:{database_mariadb_password}@{host}:3306/{database_name}"
    else:
        _sqlalchemy_database_url = lambda \
                database_name: f"mariadb+mariadbconnector://{database_mariadb_username}:{database_mariadb_password}@localhost:3306/{database_name}"
    sqlalchemy_database_url = _sqlalchemy_database_url(database_mariadb_database_name)
    database_connect_args = {}

else:
    sqlalchemy_database_url = sqlalchemy_sqlite_database_url
    database_connect_args = {"check_same_thread": False}

# --- Test Settings ---

# Yes, changing behaviour when testing is evil.
is_testing = "pytest" in sys.modules
if is_testing:
    if database_use_mariadb:
        database_mariadb_database_name = "league_clash_analyzer_test"
        sqlalchemy_database_url = _sqlalchemy_database_url("league_clash_analyzer_test")

    else:
        sqlalchemy_database_url = _sqlalchemy_database_url(
            os.path.join(working_dir_location, "eet_development_testing.db"))

# -/- Test Settings ---
