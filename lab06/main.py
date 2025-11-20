import sqlite3

# Налаштування бази даних
def init_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Створення таблиці користувачів
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            data TEXT NOT NULL
        )
    ''')

    # Додавання тестових даних
    users = [
        ('admin', 'admin123', 'ACCESS LEVEL: Admin Panel'),
        ('andrii', 'qwerty', 'ACCESS LEVEL: User Profile'),
    ]
    cursor.executemany('INSERT INTO users (username, password, data) VALUES (?, ?, ?)', users)
    conn.commit()
    return conn

# Демонстрація вразливої функції (пряма конкатенація рядків)
def vulnerable_login(conn):
    print("\n--- Вразливий вхід ---")
    username = input("Логін: ")
    password = input("Пароль: ")

    cursor = conn.cursor()
    
    sql_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    print(f"\nВиконується SQL: {sql_query}")
    
    try:
        cursor.execute(sql_query)
        users_list = cursor.fetchall() 
        
        if users_list:
            for user in users_list:
                print(f"\nУспішний вхід! Вітаємо, {user[1]}")
                print(f"    Логін: {user[1]} | Пароль: {user[2]} | Дані: {user[3]}")
        else:
            print("\nНевірний логін або пароль")
            
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

# Демонстрація захищенної функції (використання плейсхолдера (?))
def secure_login(conn):
    print("\n--- Захищений вхід ---")
    username = input("Логін: ")
    password = input("Пароль: ")

    cursor = conn.cursor()
    
    sql_query = "SELECT * FROM users WHERE username = ? AND password = ?"
    
    print(f"\nШаблон SQL: {sql_query}")
    
    try:
        cursor.execute(sql_query, (username, password))
        user = cursor.fetchone()
        
        if user:
            print(f"\nУспішний вхід! Вітаємо, {user[1]}.")
            print(f"    Логін: {user[1]} | Пароль: {user[2]} | Дані: {user[3]}")
        else:
            print("\nНевірний логін або пароль")
            
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

# Меню
def main():
    conn = init_db()
    while True:
        print("\nМеню")
        print("\n1. Вразлива версія")
        print("2. Захищена версія")
        print("3. Підказки")
        print("4. Вихід")
        
        choice = input("\nОберіть опцію: ")
        
        if choice == '1':
            vulnerable_login(conn)
        elif choice == '2':
            secure_login(conn)
        elif choice == '3':
            print("\n1. Нормальний ввід: admin")
            print("2. Виведення усіх даних: ' OR '1'='1' --")
            print("3. Обхід пароля: admin' --")
        elif choice == '4':
            conn.close()
            break
        else:
            print("Невірний вибір")

if __name__ == "__main__":
    main()