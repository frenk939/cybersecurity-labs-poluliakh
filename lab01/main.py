from run_password_check import run_password_check


def main():
    while True:
        print("\n--- Головне меню ---")
        print("1. Перевірити пароль")
        print("2. Вихід")

        choice = input("Виберіть опцію (1/2): ")

        if choice == "1":
            run_password_check()
        elif choice == "2":
            print("Дякуємо за використання програми! До побачення")
            break
        else:
            print("Невірний вибір! Спробуйте ще раз.")

if __name__ == "__main__":
    main()
