import sys
from decrypt_message import decrypt_message
from encrypt_message import encrypt_message
from generate_key import generate_key

def main():
    print("\n--- Email-шифратор ---")

    try:
        # Генерація ключа
        personal_data = input("Введіть персональні дані (пароль) для генерації ключа: ")
        
        if not personal_data:
            print("Пароль не може бути порожнім. Вихід")
            sys.exit()
            
        key = generate_key(personal_data)
        print(f"\nВаш ключ згенеровано:")
        print(f"{key.decode('utf-8')}\n")

        while True:
            print("--- Меню ---")
            print("1. Шифрувати повідомлення")
            print("2. Розшифрувати повідомлення")
            print("3. Вийти")
            choice = input("Ваш вибір (1/2/3): ").strip()

            if choice == '1':
                # Шифрування
                message = input("\nВведіть повідомлення для шифрування:\n> ")
                encrypted_token = encrypt_message(message, key)
                print("\n Повідомлення зашифровано:")
                print(encrypted_token.decode('utf-8'))
                print("-" * 20)

            elif choice == '2':
                # Розшифрування
                token_str = input("\nВведіть зашифроване повідомлення для розшифрування:\n> ")
                key_pub = input("\nВведіть ключ:\n> ")
                try:
                    # Перетворюємо скопійований рядок назад у байти
                    token_bytes = token_str.encode('utf-8')
                    decrypted_text = decrypt_message(token_bytes, key_pub)
                    
                    if decrypted_text:
                        print("\nПовідомлення розшифровано:")
                        print(decrypted_text)
                        print("-" * 20)
                except Exception:
                    print("\n[ПОМИЛКА] Формат введеного токена невірний")

            elif choice == '3':
                print("\nРоботу програми завершено")
                break

            else:
                print("\n[ПОМИЛKA] Невірний вибір. Будь ласка, введіть 1, 2 або 3")

    except KeyboardInterrupt:
        print("\n\nПрограму перервано. Вихід")
        sys.exit()

if __name__ == "__main__":
    main()