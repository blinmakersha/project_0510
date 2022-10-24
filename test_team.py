import pytest
from team_main import calculate_two


tests = [('4 * 6', 24), ('60 / 2', 30), ('4 + 78', 82), ('45 - 15', 30)]


@pytest.mark.parametrize('inp, result', tests)
def test_team_main(inp, result):
    assert calculate_two(inp) == result

