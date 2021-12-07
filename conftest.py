import pytest


def pytest_addoption(parser):
    parser.addoption("--run-slow", action="store_true", default=False)


def pytest_collection_modifyitems(config, items):
    """
    :param config:
    :param items:
    :return:
    """
    # --run-slow given in CLI.  Do not skip slow tests.
    if config.getoption("--run-slow"):
        return
    skip_slow = pytest.mark.skip(reason="Need --run-slow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
