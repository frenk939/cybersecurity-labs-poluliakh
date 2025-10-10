from hide_message import hide_message
from extract_message import extract_message


def main():
    while True:
        print("\n--- Стеганографія LSB ---")
        print("1. Приховати повідомлення в зображенні")
        print("2. Витягти повідомлення із зображення")
        print("3. Вийти")
        choice = input("Ваш вибір: ")

        if choice == '1':
            container = input("Введіть назву зображення-контейнера: ")
            message = input("Введіть ваше повідомлення (кирилиця/латиниця): ")
            output = input("Введіть ім'я для нового файлу (напр. 'output.png'): ")
            result = hide_message(container, message, output)
            print(result)
        elif choice == '2':
            stego_image = input("Введіть назву зображення: ")
            secret_message = extract_message(stego_image)
            print(f"\nЗнайдене повідомлення: {secret_message}")
        elif choice == '3':
            break
        else:
            print("Невірний вибір, спробуйте ще раз")

if __name__ == "__main__":
    main()