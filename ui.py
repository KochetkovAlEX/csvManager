def show_menu():
	print("""
	\tCsv manager
	1. Создать .csv
	2. Поиск элементов в файле
	3. Сортировка данных
	4. Добавление данных в файл
	5. Удаление данных из файла
	6. Добавление элементов в группу
	7. Вывести файл
	""")

def choice_menu():
	try:
		choice=int(input("Введите номер пункта: "))
		if 1>choice or choice>7:
			raise ValueError("Данные ложны")
		else:return choice
	except:
		raise ValueError("Данные ложны")


def show_data(input_str):
	for i in input_str.split("\n"):
		for j in i.split(";"):
			print(j,end="\t")
		print()