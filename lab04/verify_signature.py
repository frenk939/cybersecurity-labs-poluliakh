from get_hash_as_int_and_hex import get_hash_as_int_and_hex
from read_file_bytes import read_file_bytes

MODULUS = 1000007
G = 7

def verify_signature(filepath, signature, public_key):
 
    print(f"\n[Перевірка підпису]...")

    document_bytes = read_file_bytes(filepath)
    if document_bytes is None:
        print("Не вдалося прочитати файл. Перевірка неможлива")
        return False, 0, 0 
        
    current_hash, current_hex_hash = get_hash_as_int_and_hex(document_bytes)
    
    print(f"  Файл для перевірки: {filepath}")
    print(f"  Хеш поточного документа (H', hex): {current_hex_hash}")
    print(f"  Хеш поточного документа (H', int): {current_hash}")
    
    print(f"  Підпис (S): {signature}")
    print(f"  Публічний ключ (K_pub): {public_key}")

    # Ліва частина: (S * G) % P
    left_side = (signature * G) % MODULUS
    print(f"  Ліва частина (S * G) % P: {left_side}")
    
    # Права частина: (H' * K_pub) % P
    right_side = (current_hash * public_key) % MODULUS
    print(f"  Права частина (H' * K_pub) % P: {right_side}")

    is_valid = (left_side == right_side)
    
    return is_valid, left_side, right_side