from PIL import Image
from converter import text_to_binary

DELIMITER = "$$END$$"


def hide_message(image_name, message, output_image):
    try:
        img = Image.open("img/original/" + image_name)
    except FileNotFoundError:
        return "Помилка: файл зображення не знайдено."
    except Exception as e:
        return f"Помилка при відкритті зображення: {e}"

    # Додаємо делімітер, щоб знати, де закінчується повідомлення
    binary_message = text_to_binary(message + DELIMITER)
    
    # Перевіряємо, чи достатньо місця в зображенні
    max_bytes = img.width * img.height * 3
    if len(binary_message) > max_bytes:
        return "Помилка: повідомлення занадто велике для цього зображення"

    pixels = img.load()
    data_index = 0

    for y in range(img.height):
        for x in range(img.width):
            pixel = list(pixels[x, y])
            for i in range(3): # Проходимо по R, G, B
                if data_index < len(binary_message):
                    # Змінюємо найменш значущий біт
                    pixel[i] = (pixel[i] & ~1) | int(binary_message[data_index])
                    data_index += 1
            pixels[x, y] = tuple(pixel)
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break
            
    img.save("img/encrypted/" + output_image, "PNG")
    return f"Повідомлення успішно приховано у файлі {output_image}"