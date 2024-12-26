import calcu


def test_multi():
    a = 4
    b = 4
    result = calcu.multi(a, b)
    assert result == 4 * 4
    assert calcu.multi(9, 9) == 81
