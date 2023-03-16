import file
import list_func
import ui
def main():
	ui.show_menu()
	try:
		choice=ui.choice_menu()
		print(choice)
	except Exception as e:
		print(e)
		main()
main()

