from src.calc import add, div, sub, mul

def test_add() -> None:
    assert add(2, 3) == 5

def test_div() -> None:
    assert div(10, 2) == 5

def test_sub() -> None:
    assert sub(5, 2) == 3

def test_mul() -> None:
    assert mul(3, 4) == 12
