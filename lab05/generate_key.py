import hashlib
import base64


# Генерує ключ, сумісний з Fernet, з персональних даних
def generate_key(personal_data):
    # Перетворюємо пароль-рядок на байти
    password_bytes = personal_data.encode('utf-8')
    
    # Хешуємо байти пароля, отримуємо 32 байти хешу
    key_bytes = hashlib.sha256(password_bytes).digest()
    
    # Кодуємо 32-байтний хеш у base64, щоб отримати ключ Fernet
    fernet_key = base64.urlsafe_b64encode(key_bytes)
    return fernet_key