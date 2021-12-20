# [Project Euler](https://projecteuler.net/about)

Welcome to my Project Euler python practice. You can find my solutions to euler problems 
in [the problems folder](problems/euler.py). They can also be run from terminal using pytest.

The `expected_value` variable in [tests](tests/test_euler_results.py) is one I added after successfully verifying the
number from Project Euler website.

### Running Tests

in terminal, use `pytest` command to run tests.

    -v/-vv          | --verbose, Logs more information
    -q              | --quiet, Logs no information
    --duration n    | Records run times, if a number is included it will only record ones longer than n secods
    --run-slow      | Runs tests that can take more than a few seconds to run