from src.utils import unsafe_eval, greet

def test_greet():
    assert greet("Alice") == "Hello, Alice"

def test_unsafe_eval():
    # намеренно простой безопасный пример
    assert unsafe_eval("2 + 3") == 5
