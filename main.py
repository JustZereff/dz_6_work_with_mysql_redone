import os
from connection import create_connection, database

from pprint import pprint

# ok
# Знайти 5 студентів із найбільшим середнім балом з усіх предметів. Приклад - request_from_sql(request_1)
request_1 = 'request_from_msql/request_1.sql'

# ok
# Знайти студента із найвищим середнім балом з певного предмета. Назви предметів: Історія, Математика, Література, Фізика, Хімія . Приклад - request_from_sql(request_2, item='Математика')
request_2 = 'request_from_msql/request_2.sql'

# ok
# Знайти середній бал у групах з певного предмета. Приклад - request_from_sql(request_3, item='Математика')
request_3 = 'request_from_msql/request_3.sql'

# ok
# Знайти середній бал на потоці (по всій таблиці оцінок). Приклад - request_from_sql(request_4)
request_4 = 'request_from_msql/request_4.sql'

# ok
# Знайти які курси читає певний викладач. Приклад - request_from_sql(request_5, teacher_id=3)
request_5 = 'request_from_msql/request_5.sql'

# ok
# Знайти список студентів у певній групі. Приклад - request_from_sql(request_6, group_name='AA')
request_6 = 'request_from_msql/request_6.sql'

# ok
# Знайти оцінки студентів у окремій групі з певного предмета. Приклад - request_from_sql(request_7, group_name='AA', item='Історія')
request_7 = 'request_from_msql/request_7.sql'

# ok
# Знайти середній бал, який ставить певний викладач зі своїх предметів. Приклад - request_from_sql(request_8, teacher_id='3')
request_8 = 'request_from_msql/request_8.sql'

# ok
# Знайти список курсів, які відвідує студент. Приклад - request_from_sql(request_9, student_id='127')
request_9 = 'request_from_msql/request_9.sql'

# ok
# Список курсів, які певному студенту читає певний викладач. Приклад - request_from_sql(request_10, student_id='133', teacher_id='5')
request_10 = 'request_from_msql/request_10.sql'


# Створення шляху до файлу з використанням os.path.join()
request_1_path = os.path.join(os.path.dirname(__file__), request_1)
def request_from_sql(sql_file, subject=None, item=None, teacher_id=None, student_id=None, group_name=None):
    with open(sql_file, 'r', encoding='utf-8') as file:
        sql_query = file.read()
            
    with create_connection(database) as conn:
        cursor = conn.cursor()
        if teacher_id is not None and student_id is not None:
            cursor.execute(sql_query, (student_id, teacher_id))
        elif item is not None and group_name is not None:
            cursor.execute(sql_query, (group_name, item))
        elif group_name is not None and subject is not None:
            cursor.execute(sql_query, (group_name, ))
        elif teacher_id:
            cursor.execute(sql_query, (teacher_id, ))
        elif student_id:
            cursor.execute(sql_query, (student_id, ))
        elif group_name:
            cursor.execute(sql_query, (group_name, ))
        elif item:
            cursor.execute(sql_query, (item, ))
        else:
            cursor.execute(sql_query)
        data = cursor.fetchall()
        pprint(data)



if __name__ == "__main__":
    request_from_sql(request_1)