import math

x = float(input("Введите значение x: "))
n = 0
result = 0

while True:
    term = ((-1) ** n) * (x ** (2 * n + 1)) / ((2 * n + 1) * math.factorial(2 * n + 1))
    if abs(term) < 1e-10:  # Проверяем точность
        break
    result += term
    n += 1

print(f"Значение интеграла для x = {x} равно {result}")