import numpy as np


def launch_game(game_core):
    '''
        Запуск игры 1000 раз для нахождения среднего значения
        количества попыток потраченного алгоритмом для угадывания
        числа
    '''
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101,size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваша алгоритм угадывает число в среднем за {score} попыток")

    return score


def game_core_v2(number):
    '''
        Сначала устанавливаем любое число, а потом вычитаем из него разность
        между этим числом и нужным.
        Функция принимает загаданное число и возвращает число попыток
    '''

    count = 1
    predict = np.random.randint(1,101)

    while number != predict:
        count += 1
        predict = predict - (predict - number)

    return count


launch_game(game_core_v2)