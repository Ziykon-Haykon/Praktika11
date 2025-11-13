from src.utils import unsafe_eval, greet

def test_greet() -> None:
    assert greet("Alice") == "Hello, Alice"  # убрал !

def test_unsafe_eval() -> None:
    assert unsafe_eval("1 + 2") == 3
