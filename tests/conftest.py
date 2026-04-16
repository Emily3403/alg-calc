from typing import Generator

from pytest import fixture

from alg_calc.db.db_conf import DatabaseSessionMaker, init_database
from alg_calc.utils import startup


def pytest_configure() -> None:
    startup()
