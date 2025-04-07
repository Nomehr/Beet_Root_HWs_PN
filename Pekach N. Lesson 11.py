# Lesson 11
## Task 1

def new_file():
    with open('myfile.txt', 'w') as file:
        file.write ('Hello file world!\n')

def print_from_txt():
    with open('myfile.txt', 'r') as file:
        result = file.read()
        print(result)

print_from_txt()

'''
Файл myfile.txt появится в том каталоге, где был запущен скрипт.
Если к имени файла указать путь, файл будет создан или прочитает в указанной директории.
Если каталог не существует - ошибка FileNotFoundError.
'''

## Task 2

