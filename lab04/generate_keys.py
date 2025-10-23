from get_hash_as_int_and_hex import get_hash_as_int_and_hex

MODULUS = 1000007
G = 7

def generate_keys(last_name, dob, secret_word):

    print(f"\n[Генерація ключів]...")
    key_seed = f"{last_name}{dob}{secret_word}"
    print(f"  Основа ключа: {key_seed}")
    
    # Хешуємо байти рядка-основи
    private_key, hex_key_hash = get_hash_as_int_and_hex(key_seed.encode('utf-8'))
    
    # Переконуємося, що ключ не 0, бо це зламає математику
    if private_key == 0:
        private_key = 1 
    
    public_key = (private_key * G) % MODULUS
    
    print(f"  SHA256(Основа) (hex): {hex_key_hash}")
    print(f"  Приватний ключ (K_priv): {private_key}")
    print(f"  Публічний ключ (K_pub): {public_key}")
    
    return private_key, public_key