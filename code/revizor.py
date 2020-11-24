import re
import os
import os.path
import time


def parse_names_arms(path):     # получение спика армов
    files = []
    for root, dirs, file in os.walk(path):
        for filename in file:
            files.append(filename[:len(filename) - 4])
    return files


def parse_users(path,  nums_arms):  # получение имени пользователей
    lst = []
    for i in nums_arms:
        with open(path + "\\" + i + '.txt') as cs:
            name_user = re.search(r"\b\\.*", cs.read())
            lst.append(name_user.group(0)[1:])
        print(lst)
    return lst


def parse_time_date(path, nums_arms, dictionary):   # получение времени и даты сканирования
    timee = []
    datee = []
    for i in nums_arms:
        t = time.ctime(os.path.getctime(path + '\\' + i + '.txt'))
        timee.append(t[11:19])
        if t[8] == ' ':
            datee.append('0' + t[9] + '.' + dictionary[t[4:7]] + '.' + '2020')
        else:
            datee.append(t[8:10] + '.' + dictionary[t[4:7]] + '.' + '2020')
    return timee, datee


def revizor_1xp(path, nums_arms, name_user, path_to_example):   # путь до сохр. ревизоров, имена файлов, имена пользователей, пример ревизора
    special_lines = [36, 66, 81, 51]
    for i in range(len(nums_arms)):
        iterator = 0
        line22 = '<tr bgcolor=#ffffff><td align=center>' + name_user[i] + '</td><td align=center>нет</td></tr>\n'
        with open(path_to_example, encoding='cp1251') as example:
            with open(path + '\\' + nums_arms[i] + '.html', 'w', encoding='cp1251') as file:
                for line in example:
                    if iterator in special_lines:
                        file.write(name_user[i] + '\n')
                        print(file)
                    elif iterator == 22:
                        file.write(line22)
                    else:
                        file.write(line)
                    iterator += 1


def revizor_2xp(path, path_to_example, file_creation_date, file_creation_time, nums_arms, login_user):
    for i in range(len(nums_arms)):
        iterator = 0
        line17 = '<p>Пользователь:' + ' ' + login_user[i] + '<br>'
        line18 = 'Время проведения тестирования: ' + file_creation_date[i] + ' ' + file_creation_time[i] + '</p>'
        with open(path_to_example, encoding='cp1251') as example:
            with open(path + '\\' + nums_arms[i] + '.html', 'w', encoding='cp1251') as file:
                for line in example:
                    if iterator == 17:
                        file.write(line17)
                    elif iterator == 18:
                        file.write(line18)
                    elif iterator == 55:
                        file.write('(Отсутствуют)\n')
                    else:
                        file.write(line)
                    iterator += 1
