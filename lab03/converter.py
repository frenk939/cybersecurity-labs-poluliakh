def text_to_binary(text):
    # Кодуємо текст в байти за допомогою UTF-8, а потім кожен байт перетворюємо у 8-бітний двійковий формат
    return ''.join(format(byte, '08b') for byte in text.encode('utf-8'))

def binary_to_text(binary_data):
    # Розбиваємо двійковий рядок на байти (8 біт)
    byte_chunks = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    # Конвертуємо кожен байт з двійкового у ціле число
    int_values = [int(byte, 2) for byte in byte_chunks]
    # Створюємо байтовий масив та декодуємо його в текст за допомогою UTF-8
    return bytearray(int_values).decode('utf-8', 'ignore')