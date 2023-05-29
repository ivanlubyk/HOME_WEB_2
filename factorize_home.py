import multiprocessing
import time

def factorize_sync(*numbers):
    """
    Функція factorize_sync приймає список чисел та повертає список чисел,
    на які числа із вхідного списку поділяються без залишку.
    Параметри:
    numbers (int): Числа для факторизації.
    Повертає:
    list: Список чисел, на які числа з вхідного списку поділяються без залишку.
    """

    result = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        result.append(factors)
    return result

def factorize_parallel(*numbers):
    """
    Функція factorize_parallel приймає список чисел та повертає список чисел,
    на які числа із вхідного списку поділяються без залишку.
    Використовує паралельні обчислення для покращення продуктивності.
    Параметри:
    numbers (int): Числа для факторизації.
    Повертає:
    list: Список чисел, на які числа з вхідного списку поділяються без залишку.
    """

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    result = pool.map(factorize_number, numbers)
    pool.close()
    pool.join()
    return result

def factorize_number(number):
    """
    Допоміжна функція, яка обчислює список чисел, на які задане число поділяється без залишку.
    Параметри:
    number (int): Число для факторизації.
    Повертає:
    list: Список чисел, на які число поділяється без залишку.
    """

    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

if __name__ == '__main__':
    multiprocessing.freeze_support()

    start_time = time.time()
    a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
    end_time = time.time()
    execution_time_sync = end_time - start_time

    start_time = time.time()
    a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
    end_time = time.time()
    execution_time_parallel = end_time - start_time

    print("Синхронний час виконання:", execution_time_sync)
    print("Паралельний час виконання:", execution_time_parallel)
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)




