def search_in_text(text,arg,category):
    for i in text:
        i=str(i).split(";")
        if i[category]==arg:
            print(*i)
            break
    else:
        print("Элемент отсутствует")




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