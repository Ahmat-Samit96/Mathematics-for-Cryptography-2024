

# Функция для нахождения НОД и расширенного алгоритма Евклида
def extended_gcd(a, b):
    """
    Расширенный алгоритм Евклида.
    Возвращает НОД a и b, а также коэффициенты x и y такие, что:
    ax + by = gcd(a, b)
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd_value, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd_value, x, y

# Функция для нахождения решения китайской теоремы о делимых остатках
def chinese_remainder_theorem(congruences):
    """
    Решает систему конгруэнций, используя Китайскую теорему о делимых остатках.
    
    congruences - список кортежей вида (a_i, m_i), где a_i - остаток, m_i - модуль
    Возвращает решение x, которое удовлетворяет всем конгруэнциям.
    """
    # Инициализируем x = 0, N - произведение всех модулей
    x = 0
    N = 1
    for _, m in congruences:
        N *= m

    for a_i, m_i in congruences:
        # Находим N_i = N / m_i
        N_i = N // m_i
        # Находим обратное число для N_i по модулю m_i
        gcd_value, inverse, _ = extended_gcd(N_i, m_i)
        if gcd_value != 1:
            raise ValueError(f"Модули {m_i} и {N_i} не взаимно просты")
        # Добавляем к решению
        x += a_i * N_i * inverse

    return x % N

# Решение задач из задания

def solve_problem_3():
    print("Решение задачи 3. Китайская теорема о делимых остатках:")

    # 1) Решение системы:
    # x ≡ 151 (mod 255)
    # x ≡ 113 (mod 172)
    congruences_1 = [(151, 255), (113, 172)]
    solution_1 = chinese_remainder_theorem(congruences_1)
    print(f"1) Решение системы:")
    print(f"   x ≡ 151 (mod 255)")
    print(f"   x ≡ 113 (mod 172)")
    print(f"   Ответ: x = {solution_1}")

    # 2) Решение системы:
    # x ≡ 16 (mod 13)
    # x ≡ 13 (mod 37)
    # x ≡ 11 (mod 23)
    congruences_2 = [(16, 13), (13, 37), (11, 23)]
    solution_2 = chinese_remainder_theorem(congruences_2)
    print(f"\n2) Решение системы:")
    print(f"   x ≡ 16 (mod 13)")
    print(f"   x ≡ 13 (mod 37)")
    print(f"   x ≡ 11 (mod 23)")
    print(f"   Ответ: x = {solution_2}")

    # 3) Решение системы:
    # x ≡ 3 (mod 3)
    # x ≡ 3 (mod 4)
    # x ≡ 2 (mod 5)
    # x ≡ 7 (mod 11)
    congruences_3 = [(3, 3), (3, 4), (2, 5), (7, 11)]
    solution_3 = chinese_remainder_theorem(congruences_3)
    print(f"\n3) Решение системы:")
    print(f"   x ≡ 3 (mod 3)")
    print(f"   x ≡ 3 (mod 4)")
    print(f"   x ≡ 2 (mod 5)")
    print(f"   x ≡ 7 (mod 11)")
    print(f"   Ответ: x = {solution_3}")

if __name__ == "__main__":
    solve_problem_3()
