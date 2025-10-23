from get_hash_as_int_and_hex import get_hash_as_int_and_hex
from read_file_bytes import read_file_bytes

MODULUS = 1000007

def sign_document(filepath, private_key):

    print(f"\n[Підписання документа]...")
    
    document_bytes = read_file_bytes(filepath)
    if document_bytes is None:
        print("Не вдалося прочитати файл. Підписання скасовано")
        return None, None

    document_hash, hex_doc_hash = get_hash_as_int_and_hex(document_bytes)
    
    print(f"  Файл: {filepath}")
    print(f"  Хеш документа (H, hex): {hex_doc_hash}")
    print(f"  Хеш документа (H, int): {document_hash}")
    
    # Логіка підпису: S = (H * K_priv) % P
    signature = (document_hash * private_key) % MODULUS
    
    print(f"  Приватний ключ (K_priv): {private_key}")
    print(f"  Підпис (S = (H * K_priv) % P): {signature}")
    
    return signature, document_hash