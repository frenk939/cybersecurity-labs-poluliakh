from vigenere import vigenere_encrypt
from rail_fence import rail_fence_encrypt


def comparative_analysis(lang, text, key_vig, key_rf):
    enc_vig = vigenere_encrypt(text, key_vig, lang)
    enc_rf = rail_fence_encrypt(text, key_rf)

    print("\n=== Порівняльний аналіз ===")

    print("Віженер:")
    print(enc_vig)
    print("Частокол:")
    print(enc_rf)

    print("\nТаблиця порівняння:")
    print("{:<12} {:<15}".format("Метод", "Довжина"))
    print("{:<12} {:<15}".format("Віженер", len(enc_vig)))
    print("{:<12} {:<15}".format("Частокол", len(enc_rf)))