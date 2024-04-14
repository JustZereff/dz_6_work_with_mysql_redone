import sqlite3
from contextlib import contextmanager


database = './salary.db'

@contextmanager
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()
    
def drop_table(table_name):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        
        # Видалення таблиці
        cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
        
        conn.commit()

def drop_colum(table_name, colum_name):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        
        # Видалення колонки
        cursor.execute(f'''ALTER TABLE {table_name}
                            DROP COLUMN {colum_name};''')
        
        conn.commit()

def create_table():
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        
        # Создание таблицы
        cursor.execute(f'''CREATE TABLE evaluations (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            date_received TEXT,
                            history_grades TEXT,
                            math_grades TEXT,
                            literature_grades TEXT,
                            physics_grades TEXT,
                            chemistry_grades TEXT,
                            student_id INTEGER,
                            first_name VARCHAR(255) NOT NULL,
                            last_name VARCHAR(255) NOT NULL,
                            FOREIGN KEY (student_id) REFERENCES students (id) 
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE
                            )''')
        
        conn.commit()
        
def add_colum():
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        
        # Создание таблицы
        cursor.execute(f'''
                            CREATE TABLE evaluations_new (
                                id INTEGER PRIMARY KEY,
                                date_received DATE,
                                history_grades INTEGER,
                                math_grades INTEGER,
                                literature_grades INTEGER,
                                physics_grades INTEGER,
                                chemistry_grades INTEGER,
                                student_id INTEGER,
                                teacher_id INTEGER,
                                FOREIGN KEY (teacher_id) REFERENCES items(teacher_id)
                            );

                                INSERT INTO evaluations_new (id, date_received, history_grades, math_grades, literature_grades, physics_grades, chemistry_grades, student_id, teacher_id)
                                SELECT id, date_received, history_grades, math_grades, literature_grades, physics_grades, chemistry_grades, student_id, NULL AS teacher_id
                                FROM evaluations;

                                DROP TABLE evaluations;

                                ALTER TABLE evaluations_new RENAME TO evaluations;
''')
        
        conn.commit()

if __name__ == "__main__":
    # drop_table('evaluations')
    # create_table()
    # drop_colum('teachers', 'item')
    add_colum()
    # pass