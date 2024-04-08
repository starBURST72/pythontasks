def sum_odd_even_digits(n):
    odd_sum = 0
    even_sum = 0

    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        n //= 10

    return odd_sum, even_sum

n = int(input("Введите целое число в диапазоне от 0 до 10^20: "))
if 0 <= n <= 10**20:
    odd_sum, even_sum = sum_odd_even_digits(n)
    print(f"Результат – {odd_sum} {even_sum}")
else:
    print("Введенное число не находится в допустимом диапазоне.")
