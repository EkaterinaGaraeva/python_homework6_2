# 1. Создайте программу для игры в "Крестики-нолики".

import random

# создает список со значениями от 1 до 9 для обозначения ячеек
def create_field():
    field = [x for x in range(1, 10)]
    return field

# печает список в виде поля для игры
def print_field(list_with_field):
    for i in range(0, 3):
        print(f' {list_with_field[0+i*3]} | {list_with_field[1+i*3]} | {list_with_field[2+i*3]} ')
        if i < 2:
            print(f'---|---|---')
    print('\n')

# обрабытывает ход игрока
def player_move(list_with_field):
    cell_number = input('Введите номер ячейки: ')
    while True:
        try:
            cell_number = int(cell_number)
            if cell_number < 1 or cell_number > 9:
                cell_number = input('Введите номер ячейки в виде числа от 1 до 9: ')
            elif str(list_with_field[cell_number - 1]) in '0X':
                cell_number = input('Ячейка уже занята, введите другой номер: ')
            else:
                break
        except:
            cell_number = input('Введите номер ячейки в виде числа от 1 до 9: ')
    list_with_field[cell_number - 1] = '0'
    print_field(list_with_field)
    move = 1
    return list_with_field

# делает рандомный ход за бота
def bot_move(list_with_field):
    cell_number = random.randint(1, 9)
    while str(list_with_field[cell_number - 1]) in '0X':
        cell_number = random.randint(1, 9)
    else:
        list_with_field[cell_number - 1] = 'X'
    print_field(list_with_field)
    return list_with_field

# логика игры
def game(move):
    field = create_field()
    print_field(field)
    win = False
    count = 0
    while win == False or count < 10:
        if move == 0:
            player_move(field)
            count += 1
            win = cheking_win(field)
            if win == True:
                print('Выиграл игрок')
                break
            elif count == 9:
                print('Ничья')
                break
            move = 1
        elif move == 1:
            bot_move(field)
            count += 1
            win = cheking_win(field)
            if win == True:
                print('Выиграл компьютер')
                break
            elif count == 9:
                print('Ничья')
                break
            move = 0

# проверка на выигрыш
def cheking_win(list_with_field):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_coord:
        if list_with_field[i[0]] == list_with_field[i[1]] == list_with_field[i[2]]:
            return True
    return False


n = random.randint(0, 1)
game(n)