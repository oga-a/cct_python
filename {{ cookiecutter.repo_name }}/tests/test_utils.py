import pytest
from {{ cookiecutter.python_package }} import __version__


@pytest.mark.parametrize("x,sum", [(1, 2), (2, 3), (123, 124)])
def test_add_one(x: int, sum: int):
    x = {{ cookiecutter.python_package }}.utils.add_one(x)
    assert x == sum


@pytest.mark.parametrize("x,sum", [(1, 3), (2, 4), (123, 125)])
def test_add_two(x: int, sum: int):
    x = {{ cookiecutter.python_package }}.add_two(x)
    assert x == sum
