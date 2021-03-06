# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения
# на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами. Класс-исключение должен контролировать
# типы данных элементов списка. Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода пользователем очередного элемента
# необходимо реализовать проверку типа элемента. Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю
# ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class NumsOnly:
    def __init__(self, num):
        self.num = num

    list = []

    def check_num(self):
        try:
            self.num = int(self.num)
        except ValueError:
            return 'Вы ввели не число'
        else:
            NumsOnly.list.append(self.num)
            return NumsOnly.list


while True:
    input = input('Введите число или строку: ')
    if input == 'stop':
        print('Программа завершена')
        break
    else:
        object = NumsOnly(input)
        print(object.check_num())
    del input
