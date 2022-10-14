from num2words import num2words  # сторонняя библиотека для перевода числа в слово
from word2number import w2n  # сторонняя библиотека для перевода англ слова в число
from googletrans import Translator  # сторонняя библиотека для перевода с рус на англ

options = ['плюс', 'минус', 'умножить']  # список операций


def main_trans(line):
    """ перевод слова в число """

    translator = Translator()
    result = translator.translate(line)  # перевод с рус на англ
    res = result.text.split(' ')
    res = '-'.join(res)  # представление двузначного числа в виде десятки-единицы
    return w2n.word_to_num(res)


def option_in_puzzle(num1, opt, num2):
    """ действие в примере """

    if opt == 'плюс':
        return num1 + num2
    elif opt == 'минус':
        return num1 - num2
    elif opt == 'умножить':
        return num1 * num2


def calculator_base(line):
    """ основное тело программы
    число операция число
    тип str"""

    line = line.split()
    if len(line) == 1 or len(line) == 2 or len(line) == 0:
        # неправильный ввод
        return ''

    elif line[1] in options and len(line) == 3:
        # однознач + однознач
        num_1 = main_trans(line[0])
        num_2 = main_trans(line[2])
        answer = option_in_puzzle(num_1, line[1], num_2)

    elif line[2] in options and len(line) == 4:
        # многознач + однознач
        num_1 = main_trans(' '.join(line[:-2]))
        num_2 = main_trans(line[3])
        answer = option_in_puzzle(num_1, line[2], num_2)

    elif line[1] in options and len(line) == 4:
        # однознач + многознач
        num_2 = main_trans(' '.join(line[-2:]))
        num_1 = main_trans(line[0])
        answer = option_in_puzzle(num_1, line[1], num_2)

    elif line[2] in options and len(line) == 5:
        # многознач + многознач
        num_2 = main_trans(' '.join(line[-2:]))
        num_1 = main_trans(' '.join(line[:-2]))
        answer = option_in_puzzle(num_1, line[2], num_2)
    else:
        # неправильный ввод
        return ''
    return num2words(answer, lang='ru')


# --------------------------------------


def action(operation, line):
    """ промежуточное действие"""

    # проверка является ли первое число двузначным
    # и удаление использованных ненужных ячеек в списке
    if line[line.index(operation) - 1] is line[0]:
        num_1 = line[line.index(operation) - 1]
    elif line[line.index(operation) - 2] not in options:
        num_1 = line[line.index(operation) - 2] + line[line.index(operation) - 1]
        del line[line.index(operation) - 2]
    else:
        num_1 = line[line.index(operation) - 1]
    del line[line.index(operation) - 1]

    # проверка является ли второе число двузначным
    if line[line.index(operation) + 1] is line[-1]:
        num_2 = line[line.index(operation) + 1]
    elif line[line.index(operation) + 2] not in options:
        num_2 = line[line.index(operation) + 1] + line[line.index(operation) + 2]
        del line[line.index(operation) + 2]
    else:
        num_2 = line[line.index(operation) + 1]
    del line[line.index(operation) + 1]

    # составление примера в одно действие
    puzzle = num_1 + ' ' + operation + ' ' + num_2
    res = calculator_base(puzzle)

    # добавления ответа этого действия в список к основному примеру
    # путём замены значения ячейки действия
    line[line.index(operation)] = res
    return line


def calculator_long_puzzle(line):
    """ калькулятор с несколькими действиями """

    line = line.split()
    number = ''
    nums = []  # список с числами
    count_opts = 0  # подсчёт количества действий

    for i in range(len(line)):
        el = line[i]
        if el not in options:
            # проверка на двузначость числа
            number += el + ' '
            nums.append('')
        if el in options or i == len(line) - 1:
            count_opts += 1
            nums.append(main_trans(number.strip()))  # запись числа
            number = ''
            if i == len(line) - 1:
                nums.append('')

    for i in range(count_opts):
        # порядок действий
        if 'умножить' in line:
            line = action('умножить', line)
        elif 'плюс' in line:
            line = action('плюс', line)
        elif 'минус' in line:
            line = action('минус', line)
    return line[0]


print(calculator_long_puzzle('двадцать семь плюс два умножить три умножить два минус три'))
