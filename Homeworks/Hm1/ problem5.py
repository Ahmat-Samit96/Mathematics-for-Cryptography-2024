

def square_and_multiply(base, exponent, modulus):
    # Начальное значение результата
    result = 1
    # Приведение основания к модулю для упрощения вычислений
    base = base % modulus
    # Цикл выполняется, пока экспонента не станет равной нулю
    while exponent > 0:
        # Если текущая степень нечетная, умножаем результат на основание и берем модуль
        if exponent % 2 == 1:
            result = (result * base) % modulus
        # Уменьшаем экспоненту, деля на 2
        exponent = exponent // 2
        # Удваиваем основание (возводим в квадрат) и берем модуль
        base = (base * base) % modulus
    return result

def mod_inverse(a, m):
    # Используем расширенный алгоритм Евклида для нахождения обратного элемента
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    # Пока a больше 1, продолжаем вычисления
    while a > 1:
        # Вычисляем целую часть деления
        q = a // m
        # Применяем алгоритм Евклида
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    # Если x1 отрицателен, приводим его к положительному значению
    if x1 < 0:
        x1 += m0
    return x1

def decrypt_rsa(ciphertext, private_exponent, modulus):
    # Дешифрование с использованием алгоритма квадратного возведения в степень
    return square_and_multiply(ciphertext, private_exponent, modulus)

if __name__ == "__main__":
    # Заданные значения для задачи 5
    p = 179
    q = 151
    N = p * q  # Вычисляем модуль N
    phi_N = (p - 1) * (q - 1)  # Вычисляем функцию Эйлера для N
    e = 251  # Открытая экспонента
    ciphertext = 23947  # Зашифрованное сообщение

    # Вычисляем закрытую экспоненту 'd' с помощью функции mod_inverse
    d = mod_inverse(e, phi_N)

    # Дешифруем сообщение
    message = decrypt_rsa(ciphertext, d, N)
    print("5) The decrypted message (m) is:", message)
