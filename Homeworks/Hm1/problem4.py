
def square_and_multiply(base, exponent, modulus):
    # Начальное значение результата
    result = 1
    # Приведение основания к модулю для упрощения вычислений
    base = base % modulus
    # Цикл работает, пока экспонента не станет равной нулю
    while exponent > 0:
        # Если текущая степень нечетная, умножаем результат на основание и берем модуль
        if exponent % 2 == 1:
            result = (result * base) % modulus
        # Уменьшаем экспоненту, деля на 2
        exponent = exponent // 2
        # Удваиваем основание (возводим в квадрат) и берем модуль
        base = (base * base) % modulus
    return result

def modular_exponentiation(base, exponent, modulus):
    # Функция для вызова алгоритма квадратного возведения в степень
    return square_and_multiply(base, exponent, modulus)

def crt_exponentiation(base, exponent, modulus_factors):
    # Список для остатков от возведения в степень для каждого модуля
    remainders = []
    # Произведение всех модулей для вычисления общего модуля
    modulus_product = 1
    # Вычисляем остаток от возведения base^exponent по каждому модулю в списке
    for modulus in modulus_factors:
        remainders.append(modular_exponentiation(base, exponent, modulus))
        modulus_product *= modulus  # Обновляем общее произведение модулей
    
    # Переменная для хранения окончательного результата
    x = 0
    # Применяем Китайскую теорему об остатках для вычисления результата
    for i, modulus in enumerate(modulus_factors):
        Mi = modulus_product // modulus  # Вычисляем частичное произведение
        Mi_inv = pow(Mi, -1, modulus)  # Обратный элемент по модулю
        x += remainders[i] * Mi * Mi_inv  # Увеличиваем результат на текущее значение
    # Возвращаем окончательный результат по модулю общего произведения
    return x % modulus_product

if __name__ == "__main__":
    # Данные для задачи 4a
    base_4a = 13
    exponent_4a = 147
    modulus_4a = 250
    result_4a = square_and_multiply(base_4a, exponent_4a, modulus_4a)
    print("4a) Result of 13^147 mod 250 is:", result_4a)

    # Данные для задачи 4b
    base_4b = 3
    exponent_4b = 4468
    modulus_factors_4b = [13, 19, 23]
    result_4b = crt_exponentiation(base_4b, exponent_4b, modulus_factors_4b)
    print("4b) Result of 3^4468 mod 5681 is:", result_4b)
