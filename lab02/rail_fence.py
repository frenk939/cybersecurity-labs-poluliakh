def rail_fence_encrypt(text, key):
    clean_text = "".join(text.split()) 
    
    if key <= 1 or not clean_text:
        return clean_text

    rail = [[] for _ in range(key)]
    row, step = 0, 1
    
    for char in clean_text:
        rail[row].append(char)
        
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
            
        row += step
        
    return "".join("".join(r) for r in rail)

def rail_fence_decrypt(cipher, key):
    clean_cipher = "".join(cipher.split())
    n = len(clean_cipher)
    
    if key <= 1 or not clean_cipher:
        return clean_cipher

    rail = [['\n' for _ in range(n)] for _ in range(key)]
    row, step = 0, 1
    
    for col in range(n):
        rail[row][col] = '*'
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step
        
    current_cipher_index = 0
    for i in range(key):
        for j in range(n):
            if rail[i][j] == '*':
                if current_cipher_index < n:
                    rail[i][j] = clean_cipher[current_cipher_index]
                    current_cipher_index += 1

    result = []
    row, step = 0, 1
    
    for col in range(n):
        result.append(rail[row][col])
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step
        
    return "".join(result)