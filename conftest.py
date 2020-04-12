import pytest


def pytest_addoption(parser):
    parser.addoption('--run_slow', action='store_true', default=False)


def pytest_collection_modifyitems(config, items):
    """
    :param config:
    :param items:
    :return:
    """
    # --run_slow given in CLI.  Do not skip slow tests.
    if config.getoption('--run_slow'):
        return
    skip_slow = pytest.mark.skip(reason='Need --run_slow option to run')
    for item in items:
        if 'slow' in item.keywords:
            item.add_marker(skip_slow)
