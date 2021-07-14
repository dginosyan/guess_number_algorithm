# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np


def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    """Мы будем использовать алгоритм бинарного поиска.Сначала устанавливаем число по формуле,
       first + (last - first) / 2 где first и last соответственно нихнии и верхний лимит границы.
       В зависимости от того число predict меньше или больше загаданного числа, переустанавливаем новые границы
       и устанавливаем число predict по формуле."""
    count = 1
    lower_limit = 0
    upper_limit = 100

    def get_predict_number():
        return lower_limit + (upper_limit - lower_limit) // 2

    predict = get_predict_number()
    while number != predict:
        count += 1
        if number > predict:
            lower_limit = predict + 1
        elif number < predict:
            upper_limit = predict - 1
        predict = get_predict_number()
    return count  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi()
    score_game(game_core_v3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
