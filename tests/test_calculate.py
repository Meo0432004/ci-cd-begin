from calcu import multi


def test_multi():
    a = 4
    b = 4
    result = multi(a, b)
    assert result == 4 * 4
    assert multi(9, 9) == 8
    assert multi(3, 5) == 15
