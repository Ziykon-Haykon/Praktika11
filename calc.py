def add(a: int, b: int) -> int:
    """Сложение двух чисел."""
    return a + b


def div(a: int, b: int) -> float:
    """Деление двух чисел."""
    if b == 0:
        raise ValueError("На ноль делить нельзя")
    return a / b
