def calculate_product(N):
    result = 1
    if N < 0:
        return "N має бути невід'ємним числом"
    elif N == 0:
        return 1
    else:
        if N % 2 == 0:  # Перевірка на парність
            for i in range(2, N + 1, 2):
                result *= i
        else:
            for i in range(1, N + 1, 2):
                result *= i
        return result
