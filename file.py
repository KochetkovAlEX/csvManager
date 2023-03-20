def read_file(path):
	with open(path,"r",encoding="utf-8") as file:
		return file.read()
def text_create(path):
	with open(path,"r",encoding="utf-8") as file1:
		file1.readline()
		text = file1.readlines()
		return text