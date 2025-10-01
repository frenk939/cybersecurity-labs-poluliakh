from vigenere import vigenere_encrypt, vigenere_decrypt
from rail_fence import rail_fence_encrypt, rail_fence_decrypt
from analysis import comparative_analysis


def menu():
    while True:
        print("\n--- Меню ---")
        print("1. Шифрування (Віженер)")
        print("2. Розшифрування (Віженер)")
        print("3. Шифрування (Частокол)")
        print("4. Розшифрування (Частокол)")
        print("5. Порівняльний аналіз")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            lang = input("Оберіть мову (укр/en): ")
            text = input("Введіть текст: ")
            key = input("Ключ: ")
            print("Результат:", vigenere_encrypt(text, key, lang))
        elif choice == "2":
            lang = input("Оберіть мову (укр/en): ")
            text = input("Введіть зашифрований текст: ")
            key = input("Ключ: ")
            print("Результат:", vigenere_decrypt(text, key, lang))
        elif choice == "3":
            text = input("Введіть текст: ")
            key = int(input("Ключ (кількість рядків): "))
            print("Результат:", rail_fence_encrypt(text, key))
        elif choice == "4":
            text = input("Введіть зашифрований текст: ")
            key = int(input("Ключ (кількість рядків): "))
            print("Результат:", rail_fence_decrypt(text, key))
        elif choice == "5":
            lang = input("Оберіть мову (укр/en): ")
            test_text = input("Введіть текст: ")
            key_vig = input("Введіть ключ для шифру Віженера: ")
            key_rf = int(input("Введіть ключ для шифру Частоколу: "))
            comparative_analysis(lang, test_text, key_vig, key_rf)
        elif choice == "0":
            print("Вихід...")
            break
        else:
            print("Невірний вибір!")

if __name__ == "__main__":
    menu()
