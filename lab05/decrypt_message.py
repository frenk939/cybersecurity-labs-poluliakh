from cryptography.fernet import Fernet, InvalidToken


# Розшифрування повідомлень
def decrypt_message(token, key):
    try:
        f = Fernet(key)
        # Розшифровуємо токен
        decrypted_message_bytes = f.decrypt(token)
        # Перетворюємо розшифровані байти назад у рядок
        return decrypted_message_bytes.decode('utf-8')
    except InvalidToken:
        print("\n[ПОМИЛКА] Не вдалося розшифрувати. Неправильний ключ або дані пошкоджено")
        return None
    except Exception as e:
        print(f"\n[ПОМИЛКА] Введено недійсний токен (повідомлення). Переконайтеся, що скопіювали рядок повністю")
        return None