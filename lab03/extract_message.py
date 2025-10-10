from PIL import Image
from converter import binary_to_text

DELIMITER = "$$END$$"


def extract_message(image_name):
    try:
        img = Image.open("img/encrypted/" + image_name)
    except FileNotFoundError:
        return "Помилка: файл зображення не знайдено"
    except Exception as e:
        return f"Помилка при відкритті зображення: {e}"
        
    pixels = img.load()
    binary_data = ""

    for y in range(img.height):
        for x in range(img.width):
            pixel = pixels[x, y]
            for i in range(3): # R, G, B
                # Витягуємо останній біт і додаємо до рядка
                binary_data += str(pixel[i] & 1)

    # Декодуємо дані та шукаємо делімітер
    try:
        full_text = binary_to_text(binary_data)
        if DELIMITER in full_text:
            return full_text.split(DELIMITER)[0]
        else:
            return "Помилка: делімітер кінця повідомлення не знайдено"
    except Exception as e:
        return f"Помилка декодування: {e}"