import os
import file
import list_func
import ui
def main():
	os.system("cls")
	ui.show_menu()
	file.read_file("data.csv")
	try:
		choice=ui.choice_menu()
		print(choice)
		if choice==7:
			ui.show_data(file.read_file("data.csv"))
			input()
			main()
		elif choice==2:
			category=ui.show_category("data.csv")
			arg=input("Что ищем? ")
			list_func.search_in_text(file.text_create("data.csv"),arg,category) #поиск и показ строк в файле
			print()
		elif choice ==4:
			id=input("Введите id города: ")
			city = input("Введите название города: ")
			region = input("Введитфе Регион города: ")
			district = input("Введите округ города: ")
			population = input("Введите население города: ")
			foundation = input("Введите дату основания города: ")
			file.write_down("data.csv",ui.create_new_line(id,city,region,district,population,foundation))
			print("Файл изменён")
		elif choice==5:
			id=input("Введите id удаляемой строки: ")
			text=file.text_create("data.csv")
			file.rewrite_file("data.csv",list_func.remove_line(id,text))
			print("Файл изменён")
		elif choice==3:
			arg = input("Общий признак ")
			list_func.unite(file.text_create("data.csv"),arg)
			print()
		elif choice == 1: #создает новый на основе сущесвтующего
			name=input("Введите имя файла: ")
			file.new_file(name,file.text_create("data.csv"))
			print()
		elif choice==6:
			arg=input("Общий признак ")
			list_func.choice(file.text_create("data.csv"),arg)
			print()
		input()
		main()
	except Exception as er:
		print(er)
		input()
		main()
main()