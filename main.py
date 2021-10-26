
import time
time = time.ctime()
time = time.replace(" ", '_')
time = time.replace(":", '-')
output_file_name = f"{time}_output.csv"

print(time)


dict_list = []
text = ""


def get_data_from_dict():
    with open('dict.txt') as file_object:
        for line in file_object:
            line = line.replace('\n', '')
            line = line.lower()
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
        get_count_of_each_sumbol(dict_list, text, len_text)


def get_count_of_each_sumbol(dict_list, text, len_text):
    local_len_text = 0
    for sumbol in dict_list:
        i = text.count(sumbol)
        local_len_text = i + local_len_text
        print(f"{sumbol} {i} шт")
        with open(output_file_name, 'a') as f:
            f.write(f"{sumbol}\t{i}\n")
    print(
        f"Всего символов в исходном файле text.txt найдено {len_text} \nСовпадений со словарем найдено {local_len_text}\nФайл {output_file_name} сохранен")



if __name__ == "__main__":
    get_data_from_dict()
    get_data_from_text()
