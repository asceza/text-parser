dict_list = []
text = ""


def get_data_from_dict():
    with open('dict.txt') as file_object:
        for line in file_object:
            line = line.replace('\n', '')
            dict_list.append(line)


def get_data_from_text():
    with open('text.txt') as file_object:
        text = file_object.read()
        text = text.lower()
        l = len(text)
        text = text.replace(" ", "")
        l = l - len(text)
        print(f"Удаляем {l} пробелов")
        l = len(text)
        text = text.replace("\n", "")
        l = l - len(text)
        print(f"Удаляем {l} переносов строки")
        l = len(text)
        text = text.replace("\t", "")
        l = l - len(text)
        print(f"Удаляем {l} символов табуляции")
        len_text = len(text)
        get_count_of_each_sumbol(dict_list, text)


def get_count_of_each_sumbol(dict_list, text):
    local_len_text = 0
    for sumbol in dict_list:
        text = text.replace(sumbol, "")
    print(f"Эти символы остутствуют в файле dict.txt:\n{text}")


if __name__ == "__main__":
    get_data_from_dict()
    get_data_from_text()
