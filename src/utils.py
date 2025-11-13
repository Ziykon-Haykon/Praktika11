# Потенциальная проблема: небезопасное использование eval
def unsafe_eval(expr: str):
    return eval(expr)  # Bandit B307

# Функция с пропущенной аннотацией
def greet(name):
    return f"Hello, {name}"
