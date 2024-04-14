import datetime
from random import randint
from connection import create_connection, database


from faker import Faker


fake_data = Faker(locale="uk-UA")
fake = Faker()

COUNTER = 500


# print(fake_data.name())

def insert_data(connection, sql_query):
    cursor = connection.cursor()
    cursor.executemany(sql_query, [(fake_data.name(),) for _ in range(COUNTER)])
    connection.commit()
    
def insert_disciplines(connection):
    cursor = connection.cursor()
    disciplines = [
        ("Історія",),
        ("Математика",),
        ("Література",),
        ("Фізика",),
        ("Хімія",)
    ]
    cursor.executemany("INSERT INTO disciplines(name) VALUES (?)", disciplines)
    connection.commit()
    
def insert_grades(connection):
    cursor = connection.cursor()
    # Отримання списку discipline_id та student_id
    cursor.execute("SELECT id FROM disciplines")
    discipline_ids = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT id FROM students")
    student_ids = [row[0] for row in cursor.fetchall()]

    # Заповнення таблиці оцінок
    for _ in range(COUNTER):
        # Випадково вибираємо discipline_id та student_id
        discipline_id = randint(1, len(discipline_ids))
        student_id = randint(106, 150)
        # Генеруємо випадкову оцінку та дату
        grade = randint(1, 5)
        date_of = datetime.date(randint(2010, 2024), randint(1, 12), randint(1, 28))

        # Вставка оцінки в таблицю
        cursor.execute("INSERT INTO grades(discipline_id, student_id, grade, date_of) VALUES (?, ?, ?, ?)",
                       (discipline_id, student_id, grade, date_of))
    connection.commit()


if __name__ == "__main__":
    # Генерація предметів та оцінок
    # with create_connection(database) as conn:
    #     insert_grades(conn)
        
    # --------------------------------------------------------------------------------------------
        
    #   Цим запитом з деякими корегуваннями я заповнював таблиці Студентів та Вчителів
    # sql_query = """
    # INSERT OR IGNORE INTO teachers(fullname)
    # VALUES (?)
    # """
    # with create_connection(database) as conn:
    #     insert_data(conn, sql_query)
    
    
        
    pass