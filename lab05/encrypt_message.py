from cryptography.fernet import Fernet


# Шифрування тексту
def encrypt_message(message, key):
    f = Fernet(key)
    # Шифруємо повідомлення
    encrypted_message = f.encrypt(message.encode('utf-8'))
    return encrypted_message