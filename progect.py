import random
def readlines(file):
        lines = file.readlines()
        while True:
    try:
        questionCount = int(input('количество заданий'))
        if questionCount >= 1:
            break
        print('пожалуйста введите другое число')
        while True:
    print('выберите тип задания')
