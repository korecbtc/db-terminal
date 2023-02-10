import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()


def create_table():
    """Создание таблицы"""
    cur.execute('''
    CREATE TABLE IF NOT EXISTS people(
    id INTEGER PRIMARY KEY,
    name TEXT,
    birthday INTEGER,
    gender TEXT
    );
    ''')


def insert(string):
    """Ввод значений в таблицу"""
    cur.execute(
        '''INSERT INTO people
        VALUES((SELECT COUNT(*) + 1 FROM people), ?, ?, ?);''',
        string
    )


def select():
    """Вывод значений"""
    print('№---------ФИО---------Дата рождения--Пол')
    cur.execute('''
        SELECT DISTINCT id, name, birthday, gender
        FROM people
        ORDER BY name
        LIMIT 100;
        ''')
    count = 0
    for result in cur:
        print(*result)
        count += 1
    if count == 0:
        print('В базе нет ни одной записи')


def find(last_name):
    """Поиск записи по фамилии"""
    print('№------ФИО---------Дата рождения--Пол')
    cur.execute(f'''
        SELECT id, name, birthday, gender
        FROM people
        WHERE name LIKE '{last_name}%'
        ORDER BY name
        LIMIT 100;
        ''')
    count = 0
    for result in cur:
        print(*result)
        count += 1
    if count == 0:
        print('Не найдено ни одной записи')


def delete(string):
    """Удаление записи"""
    cur.execute(f'''
        DELETE
        FROM people
        WHERE id LIKE '{int(string[0])}';
        ''')


def input_data():
    """Ввод команд"""
    while True:
        try:
            command = input('Введите команду:')
            string = command.split()[1:]
            name = ' '.join(string[:3])
            string = [name] + string[3:]
            action = command.split()[0]

            if action == 'add':
                insert(string)
            elif action == 'show_all':
                select()
            elif action == 'find':
                find(string[0])
            elif action == 'delete':
                delete(string)
            elif action == 'quit':
                print('До свидания!')
                break
            else:
                print('Введите команду в формате:\n'
                      'Создание записи - '
                      '<add Ivanov Ivan Sergeevich 1987-09-11 M>\n'
                      'Вывод записей таблицы - <show_all>\n'
                      'Поиск по фамилии - <find Ivanov>\n'
                      'Удаление записи - <delete '
                      'Ivanov Ivan Sergeevich 1987-09-11 M>\n'
                      'Выход - <quit>')
        except Exception:
            print('Введите команду в формате:\n'
                  'Создание записи - '
                  '<add Ivanov Ivan Sergeevich 1987-09-11 M>\n'
                  'Вывод записей таблицы - <show_all>\n'
                  'Поиск по фамилии - <find Ivanov>\n'
                  'Удаление записи - <delete '
                  'Ivanov Ivan Sergeevich 1987-09-11 M>\n'
                  'Выход - <quit>')


if __name__ == '__main__':
    create_table()
    input_data()
    con.commit()
    con.close()
