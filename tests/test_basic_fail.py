from arithmetic.basic import sum, diff, mult

def test_sum_fail():
    assert sum(1,2) == 0

def test_diff_fail():
    assert diff(3,1) == 0

def test_mult_fail():
    assert mult(-5, 3) == 0


