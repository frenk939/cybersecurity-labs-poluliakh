from generate_keys import generate_keys
from sign_document import sign_document
from verify_signature import verify_signature
from read_file_bytes import read_file_bytes

def main_menu():

    current_private_key = None
    current_public_key = None
    current_document_path = None 
    current_signature = None

    while True:
        print("\n--- ГОЛОВНЕ МЕНЮ ---")
        print("1. Згенерувати пару ключів (Приватний/Публічний)")
        print("2. Вказати файл для роботи")
        print("3. Підписати поточний файл (Приватним ключем)")
        print("4. Перевірити підпис поточного файлу (Публічним ключем)")
        print("5. Вихід")
        
        choice = input("Ваш вибір (1-5): ")

        if choice == '1':
            # --- 1. Генерація ключів ---
            print("\n--- 1. Генерація ключів ---")
            last_name = input("  Ім\'я: ")
            dob = input("  Дата народження (ДД.ММ.РРРР): ")
            secret = input("  Секретне слово: ")
            
            if not all([last_name, dob, secret]):
                print("Помилка: Усі поля є обов'язковими")
                continue
                
            current_private_key, current_public_key = generate_keys(last_name, dob, secret)
            current_signature = None 

        elif choice == '2':
            # --- 2. Вказати файл ---
            print("\n--- 2. Вказати файл для роботи ---")
            filepath = input("Введіть повний або відносний шлях до файлу:\n")
            
            if read_file_bytes(filepath) is not None:
                current_document_path = filepath
                current_signature = None 
                print(f"Файл '{current_document_path}' успішно обрано")
            else:
                print(f"Не вдалося отримати доступ до файлу")

        elif choice == '3':
            # --- 3. Підписання файлу ---
            print("\n--- 3. Підписання файлу ---")
            if current_private_key is None:
                print("Помилка: Спочатку згенеруйте ключі (Пункт 1)")
                continue
            if current_document_path is None:
                print("Помилка: Спочатку вкажіть файл (Пункт 2)")
                continue
                
            signature, original_hash = sign_document(current_document_path, current_private_key)
            if signature is not None:
                current_signature = signature
                print(f"Підпис створено. Оригінальний хеш (int): {original_hash}")

        elif choice == '4':
            # --- 4. Перевірка підпису ---
            print("\n--- 4. Перевірка підпису ---")
            if current_signature is None:
                print("Помилка: Файл ще не підписано (Пункт 3)")
                continue
            if current_document_path is None:
                print("Помилка: Файл не вказано (Пункт 2)")
                continue
            # Для перевірки потрібен ПУБЛІЧНИЙ ключ
            if current_public_key is None: 
                print("Помилка: Ключі не згенеровано (Пункт 1)")
                continue

            # Передаємо ПУБЛІЧНИЙ ключ
            is_valid, _, _ = verify_signature(current_document_path, current_signature, current_public_key)
            
            if is_valid:
                print("\n[РЕЗУЛЬТАТ]: Підпис ДІЙСНИЙ. Файл не змінювався")
            else:
                print("\n[РЕЗУЛЬТАТ]: Підпис ПІДРОБЛЕНИЙ! Файл було змінено або файл не читається")

        elif choice == '5':
            # --- 5. Вихід ---
            print("Завершення роботи...")
            break
            
        else:
            print(" Невірний вибір. Будь ласка, введіть число від 1 до 5")

# --- Точка входу в програму ---
if __name__ == "__main__":
    main_menu()