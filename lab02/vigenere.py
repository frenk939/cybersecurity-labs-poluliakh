UK_ALPHABET = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ" 
EN_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vigenere_encrypt(text, key, lang): 
    if lang == "en":
        ALPHABET = EN_ALPHABET
        ALPH_LEN = len(EN_ALPHABET)
    else:
        ALPHABET = UK_ALPHABET
        ALPH_LEN = len(UK_ALPHABET)
    result = [] 
    key = key.upper() 
    key_index = 0 
    for char in text: 
        if char.upper() in ALPHABET: 
            shift = ALPHABET.index(key[key_index % len(key)]) 
            idx = ALPHABET.index(char.upper()) 
            enc_char = ALPHABET[(idx + shift) % ALPH_LEN] 
            result.append(enc_char if char.isupper() else enc_char.lower()) 
            key_index += 1 
        else: 
            result.append(char) 
    return "".join(result)

def vigenere_decrypt(text, key, lang):
    if lang == "en":
        ALPHABET = EN_ALPHABET
        ALPH_LEN = len(EN_ALPHABET)
    else:
        ALPHABET = UK_ALPHABET
        ALPH_LEN = len(UK_ALPHABET) 
    result = [] 
    key = key.upper() 
    key_index = 0 
    for char in text: 
        if char.upper() in ALPHABET: 
            shift = ALPHABET.index(key[key_index % len(key)]) 
            idx = ALPHABET.index(char.upper()) 
            dec_char = ALPHABET[(idx - shift) % ALPH_LEN] 
            result.append(dec_char if char.isupper() else dec_char.lower()) 
            key_index += 1 
        else: 
            result.append(char) 
    return "".join(result)