def search_in_text(text,arg,category):
    for i in text:
        i=str(i).split(";")
        if i[category].startswith(arg):
            print(*i)
            break
    else:
        print("Элемент отсутствует")
