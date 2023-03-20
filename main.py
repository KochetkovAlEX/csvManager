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
			print("id", "city", "region", "district", "population", "foundation")
			arg = input("Поиск среди чего? ").lower()
			search = input("Что ищем? ")
			ui.search_in_text(file.text_create("data.csv"),arg,search)
			input()
			main()
	except Exception as er:
		print(er)
		input()
		main()
main()