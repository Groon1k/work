import revizor

path_to_freepc = input('enter your path to FreePC: ')
path_to_folder_with_CS_revizor_1_XP = input('enter your path to Revizor 1XP: ')  # куда сохранять файлы ревизоров
path_to_rev1xp = input(
    'enter the path to the \"Revizor 1XP\" sample file along with the name of this file: ')  # путь до файла с самим файлом ревизора 1ХР откуда будет браться основа
path_to_folder_with_CS_revizor_2_XP = input('enter your path to Revizor 2XP: ')
path_to_rev2xp = input(
    'enter the path to the \"Revizor 2XP\" sample file along with the name of this file: ')  # путь до файла с самим файлом ревизора 2ХР откуда будет браться основа                                                                                                                    # такую же конструкцию как в файле, сверху сам комп, снизу флешка

MonthDict = {"Jan": '01',
             "Feb": '02',
             "Mar": '03',
             "Apr": '04',
             "May": '05',
             "Jun": '06',
             "Jul": '07',
             "Aug": '08',
             "Sep": '09',
             "Oct": '10',
             "Nov": '11',
             "Dec": '12'
             }
lst_nums_arms = revizor.parse_names_arms(path_to_freepc)
print(lst_nums_arms)
lst_name_user = revizor.parse_users(path_to_freepc, lst_nums_arms)
print(lst_name_user)
lst_time_scan, lst_date_scan = revizor.parse_time_date(path_to_freepc, lst_nums_arms, MonthDict)
print('lst time:', lst_time_scan, 'lst date:', lst_date_scan)
revizor.revizor_1xp(path_to_folder_with_CS_revizor_1_XP, lst_nums_arms, lst_name_user, path_to_rev1xp)
revizor.revizor_2xp(path_to_folder_with_CS_revizor_2_XP, path_to_rev2xp, lst_date_scan, lst_time_scan, lst_nums_arms,
                    lst_name_user)

