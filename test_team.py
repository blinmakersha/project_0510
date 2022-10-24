import pytest
from additional_func import calculate


tests = [('4 * 6', 24), ('60 / 2', 30), ('4 + 78', 82), ('45 - 15', 30)]


@pytest.mark.parametrize('inp, answer', tests)
def test_team_main(inp, answer):
    first, sym, snd = inp.split()
    assert calculate(first, sym, snd) == answer

