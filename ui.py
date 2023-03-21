import file


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
			s=len(j)
			print(j,end="\t"*(5-s//4))
		print()



def show_category(path):
	line=file.read_line(path).split(";")
	line[len(line)-1]=line[len(line)-1][:-1:]
	print("Выберите категорию:")
	for i in line:
		print(i,end=" ")
	choice=input()
	if choice in line:
		return line.index(choice)
	else: raise ValueError("Данные ложны")

def create_new_line(id,city,region,district,population,foundation):
    line = [id + ";", city + ";", region + ";", district + ";", population + ";", foundation+"\n"]
    return line