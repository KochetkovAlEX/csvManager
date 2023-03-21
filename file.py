def read_file(path):
	with open(path,"r",encoding="utf-8") as file:
		return file.read()
def text_create(path):
	with open(path,"r",encoding="utf-8") as file1:
		file1.readline()
		text = file1.readlines()
		return text
def read_line(path):
	with open(path,"r",encoding="utf-8") as file1:
		return file1.readline()

def write_down(path,line):
	with open(path,"a",encoding="utf-8") as file1:
		for i in line:
			file1.write(i)
	return file1

def rewrite_file(path,text):
	with open(path,"w",encoding="utf-8") as file1:
		for i in text:
			file1.write(i)
	return file1