# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее. Подсказка: используйте функцию count() и cycle()
# модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие
# его завершения. #### Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import cycle, count

# а) итератор, генерирующий целые числа, начиная с указанного
list = []
for i in count(3):
    list.append(i)
    if i == 10:
        break
print(list)

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
for i in cycle(list):
    if i == 10:
        print(i)
        break
    else:
        print(i)
