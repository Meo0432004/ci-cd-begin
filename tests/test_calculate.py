from calcu import multi


def test_multi():
    a = 4
    b = 4
    result = multi(a, b)
    assert result == 4 * 4
