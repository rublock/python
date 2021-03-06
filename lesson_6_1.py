# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
import time

color_list = ['красный', 'желтый', 'зеленый']
time_list = [7, 2, 10]

class TrafficLight:

	def __init__(self, __color, time):
		self.__color = __color
		self.time = time

	def running(self):
		time.sleep(self.time)
		return f'{self.__color} горел {self.time} сек.'
		
for i, n in zip(color_list, time_list):
	run = TrafficLight(i, n)
	print(run.running())
	