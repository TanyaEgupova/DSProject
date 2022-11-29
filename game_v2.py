

import numpy as np


def random_predict(number: int = np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    start = 1
    end = 100

    while True:
        count += 1
        predict_number =  (start + end)//2 # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        elif (number > predict_number):
            start = predict_number
        else:
            end = predict_number
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

# RUN
if __name__ == "_main_":
    score_game(random_predict)
    