# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:
import sqlite3

def create_students_table(db_name):
    con = sqlite3.connect("teatchers.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE Students(Student_Id INTEGER, Student_Name TEXT, School_Id INTEGER PRIMARY KEY)")
    cur.execute("""INSERT INTO Students VALUES 
    (201, "Иван", 1),
    (202, "Петр", 2),
    (203, "Анастасия", 3),
    (204, "Игорь", 4)
    """)
    con.commit()