from mod import calculate_product

N = int(input("Введіть невід'ємне ціле число N: "))

result_product = calculate_product(N)
if isinstance(result_product, str):
    print(result_product)
else:
    if N % 2 == 0:
        print(f"Добуток парних чисел від 2 до {N}: {result_product}")
    else:
        print(f"Добуток непарних чисел від 1 до {N}: {result_product}")

