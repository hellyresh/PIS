print("Задание 1\nНайти N-й член последовательности 1, 1, 2, 3, 5, 8, 13...")


def find_fib_num(n):
    num1 = 1
    num2 = 1
    for _ in range(2, n):
        sum = num1 + num2
        num1 = num2
        num2 = sum
    return num2


print("1-й:", find_fib_num(1), ", 3-й:", find_fib_num(3), ", 9-й:", find_fib_num(9))
print("\nЗадание 2\nНайти N-й член последовательности 1, 1, 1, 3, 5, 9, 17…")


def find_num(n):
    num1 = 1
    num2 = 1
    num3 = 1
    for _ in range(3, n):
        print(num1)
        sum = num1 + num2 + num3
        num1 = num2
        num2 = num3
        num3 = sum
    return num3


print("1-й:", find_num(1), ", 3-й:", find_num(3), ", 9-й:", find_num(9))
print("\nЗадание 3\nВывести квадраты нечетных чисел до N. (генератором списков)")


def square_odd_list(n):
    l = [i ** 2 for i in range(1, n + 1, 2)]
    return l


print("Ответ:", square_odd_list(16))
print("\nЗадание 4\nВычислить сумму и произведение всех натуральных чисел от А до В включительно")


def sum_prod(a, b):
    sum = 0
    prod = 1
    for i in range(a, b + 1):
        sum += i
        prod *= i
    return [sum, prod]


res = sum_prod(3, 10)
print("A = 3, B = 10\nСумма:", res[0], "\nПроизведение:", res[1])
print("\nЗадание 5\nДаны натуральные числа А и В. Вывести сначала все чётные числа, заключённые "
      "между ними, потом все нечётные (генератором/ами списков)")


def even_odd_nums(a, b):
    even = [i for i in range(a, b + 1) if i % 2 == 0]
    odd = [i for i in range(a, b + 1) if i % 2 != 0]
    return [even, odd]


res = even_odd_nums(10, 20)
print("A = 10, B = 20\nЧетные:", res[0], "\nНечетные:", res[1])
print("\nЗадание 6\nИсходный список содержит положительные и отрицательные числа. "
      "Требуется положительные поместить в один список, а отрицательные - в другой (генератором/ами списков)")


def pos_neg_nums(l):
    pos = [i for i in l if i > 0]
    neg = [i for i in l if i < 0]
    return [pos, neg]


res = pos_neg_nums([0, 4, -6, 19, -5, 300, 71, -45, -1, 23, 43, 91, -75, -1000])
print("Исходный список: [0, 4, -6, 19, -5, 300, 71, -45, -1, 23, 43, 91, -75, -1000]")
print("Положительные:", res[0], "\nОтрицательные:", res[1])
