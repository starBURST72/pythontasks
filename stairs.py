def print_stairs(n):
    for i in range(1, n + 1):
        print('#' * i)

n = int(input("Введите целое число в диапазоне от 1 до 20: "))
if 1 <= n <= 20:
    print_stairs(n)
else:
    print("Введенное число не находится в допустимом диапазоне.")
