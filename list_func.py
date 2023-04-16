def search_in_text(text,arg,category):
    for i in text:
        i=str(i).split(";")
        if i[category]==arg:
            print(*i)
            break
    else:
        print("Элемент отсутствует")

def unite(text,arg):
    lst=[]
    for i in text:
        if arg in str(i):
            if str(i).endswith("\n"): i=i[:-1]
            lst.append(i)
    print(*lst)
def remove_line(id,text):
    if len(text)==id:
        for i in text:
            a= str(i).split(";")
            if a[0] == id:
                text.remove(i)
                return text
            elif a[0]!=id:
                print("id отсутсвует")
                break
    else:
        print("0")

def choice(text,arg):
    list1=[]
    for i in text:
        if arg in str(i):
            if str(i).endswith("\n"): i=i[:-1]
            list1.append(i)
            arg=input("Введите признак: ")
        if arg=="/":
            print(list1)
            break
