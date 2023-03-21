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
			list_func.search_in_text(file.text_create("data.csv"),arg,category)
			print()
			input()
			main()
	except Exception as er:
		print(er)
		input()
		main()
main()