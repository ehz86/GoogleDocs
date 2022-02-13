# для реализации задачи, я использую библиотеку gspread
import gspread
# Указываем путь к JSON
gc = gspread.service_account(filename='example.json')
#Открываем тестовую таблицу откуда, я беру всю информацию
sh = gc.open("Тестовая таблица")
#Создаю лист и собираю всю информацию в виде списка
worksheet = sh.sheet1
list_of_lists = worksheet.get_all_values()
#Открываю новую таблицу, создаю в ней лист, и заполняю диапазон ячеек значениями из списка
sh2 = gc.open("Новая таблица")
worksheet2 = sh2.sheet1
worksheet2.update('A1:B7', list_of_lists)