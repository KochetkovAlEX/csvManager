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
			print(j,end="|")
		print()

def search_in_text(text,arg,search):
	for i in text:
		i = i.split(";")
		if arg == 'id':
			if i[0].startswith(search):
				print(*i)
				break
		elif arg == 'city':
			if i[1].startswith(search):
				print(*i)
				break
		elif arg == 'region':
			if i[2].startswith(search):
				print(*i)
				break
		elif arg == 'district':
			if i[3].startswith(search):
				print(*i)
		elif arg == 'population':
			if i[4].startswith(search):
				print(*i)
				break
		elif arg == 'foundation':
			if i[5].startswith(search):
				print(*i)
				break
		elif arg == 'numb':
			if i[6].startswith(search):
				print(*i)
				break
		else:
			print("данного аргумента нет")
			break
