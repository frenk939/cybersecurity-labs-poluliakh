import os
import time
import base64
from getpass import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from PIL import Image

# Шифрування (AES)
class CryptoModule:
    def __init__(self):
        self.salt = b'lab_work_7_salt'

    def generate_key(self, password):
        # Генерує ключ шифрування на основі пароля 
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    def encrypt_data(self, data, password):
        key = self.generate_key(password)
        f = Fernet(key)
        return f.encrypt(data)

    def decrypt_data(self, encrypted_data, password):
        key = self.generate_key(password)
        f = Fernet(key)
        return f.decrypt(encrypted_data)

# Стеганографія (LSB)
class StegoModule:
    def data_to_bin(self, data):
        # Конвертує байти у бінарний рядок
        if isinstance(data, str):
            return ''.join([format(ord(i), "08b") for i in data])
        elif isinstance(data, bytes):
            return ''.join([format(i, "08b") for i in data])
        return data

    def hide_data(self, image_path, data, output_path):
        # Ховає байти даних у зображення
        image = Image.open(image_path)
        # Конвертуємо зображення в RGB, щоб мати 3 канали
        image = image.convert("RGB")
        
        # Додаємо стоп-маркер, щоб знати, де закінчується файл
        stop_marker = b'===END==='
        full_data = data + stop_marker
        binary_data = self.data_to_bin(full_data)
        data_len = len(binary_data)
        
        pixels = list(image.getdata())
        max_capacity = len(pixels) * 3
        
        if data_len > max_capacity:
            raise ValueError(f"Файл завеликий для цього зображення. Потрібно пікселів: {data_len/3}, є: {len(pixels)}")

        new_pixels = []
        data_index = 0

        for pixel in pixels:
            if data_index < data_len:
                r, g, b = pixel
                
                # Модифікуємо LSB кожного кольору
                if data_index < data_len:
                    r = int(bin(r)[2:-1] + binary_data[data_index], 2)
                    data_index += 1
                if data_index < data_len:
                    g = int(bin(g)[2:-1] + binary_data[data_index], 2)
                    data_index += 1
                if data_index < data_len:
                    b = int(bin(b)[2:-1] + binary_data[data_index], 2)
                    data_index += 1
                
                new_pixels.append((r, g, b))
            else:
                new_pixels.append(pixel)

        image.putdata(new_pixels)
        image.save(output_path, "PNG")
        return True

    def extract_data(self, image_path):
        # Витягує дані із зображення
        image = Image.open(image_path)
        image = image.convert("RGB")
        pixels = list(image.getdata())

        binary_data = ""
        for pixel in pixels:
            r, g, b = pixel
            binary_data += bin(r)[-1]
            binary_data += bin(g)[-1]
            binary_data += bin(b)[-1]

        # Конвертуємо біти назад у байти
        all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
        
        decoded_data = b""
        stop_marker = b'===END==='
        
        # Шукаємо стоп-маркер
        temp_bytes = b""
        for byte in all_bytes:
            try:
                int_byte = int(byte, 2)
                temp_bytes += int_byte.to_bytes(1, byteorder='big')
                if temp_bytes.endswith(stop_marker):
                    decoded_data = temp_bytes[:-len(stop_marker)]
                    break
            except:
                pass
                
        return decoded_data

# Аналітика та головна логіка
class SecuritySystem:
    def __init__(self):
        self.crypto = CryptoModule()
        self.stego = StegoModule()
        self.metrics = []

    def get_file_size(self, path):
        return os.path.getsize(path) if os.path.exists(path) else 0

    def protect_process(self):
        print("\n--- Етап захисту ---")
        input_file = input("Введіть відносний шлях до файлу для захисту: ")
        cover_image = input("Введіть відносний шлях до зображення: ")
        password = getpass("Введіть пароль для шифрування: ")

        if not os.path.exists(input_file) or not os.path.exists(cover_image):
            print("Помилка: Файл або картинка не існують")
            return

        try:
            # Читання
            start_total = time.time()
            with open(input_file, 'rb') as f:
                file_data = f.read()
            original_size = len(file_data)
            print(f"  Файл прочитано. Розмір: {original_size / 1024:.2f} КБ")

            # Шифрування
            t1 = time.time()
            encrypted_data = self.crypto.encrypt_data(file_data, password)
            enc_time = time.time() - t1
            enc_size = len(encrypted_data)
            print(f"  Етап 1 завершено: шифрування AES. Час: {enc_time:.4f} с. Новий розмір: {enc_size / 1024:.2f} КБ")

            # Стеганографія
            output_stego = "protected_container.png"
            t2 = time.time()
            self.stego.hide_data(cover_image, encrypted_data, output_stego)
            stego_time = time.time() - t2
            final_size = self.get_file_size(output_stego)
            print(f"  Етап 2 завершено: стеганографія. Час: {stego_time:.4f} с.")

            total_time = time.time() - start_total
            
            # Логування метрик
            self.metrics.append({
                "operation": "Захист",
                "file": input_file,
                "enc_time": enc_time,
                "stego_time": stego_time,
                "total_time": total_time,
                "orig_size": original_size,
                "final_size": final_size
            })
            
            print(f"  Файл успішно захищено у '{output_stego}'")

        except Exception as e:
            print(f"Сталася помилка: {e}")

    def restore_process(self):
        print("\n--- Етап відновлення ---")
        stego_image = input("Введіть відносний шлях до стегоконтейнера: ")
        output_file = input("Введіть назву для відновленого файлу (напр. restored.txt): ")
        password = getpass("Введіть пароль для розшифрування: ")

        if not os.path.exists(stego_image):
            print("Помилка: Файл не існує")
            return

        try:
            start_total = time.time()

            # 1. Витягування
            print("  Початок витягування даних з зображення...")
            t1 = time.time()
            extracted_data = self.stego.extract_data(stego_image)
            extract_time = time.time() - t1
            
            if not extracted_data:
                print("  Не вдалося знайти приховані дані або маркер.")
                return

            print(f"  Дані витягнуто. Розмір: {len(extracted_data)} байт")
            
            # Демонстрація необхідності обох етапів
            print(">>> ДЕМОНСТРАЦІЯ: Спроба прочитати дані без дешифрування...")
            print(f">>> Перші байти: {extracted_data[:20]}")

            # Розшифрування
            t2 = time.time()
            try:
                decrypted_data = self.crypto.decrypt_data(extracted_data, password)
            except Exception:
                print("  Невірний пароль! Розшифрування неможливе")
                return
            decrypt_time = time.time() - t2

            with open(output_file, 'wb') as f:
                f.write(decrypted_data)

            total_time = time.time() - start_total

            self.metrics.append({
                "operation": "Відновлення",
                "file": output_file,
                "extract_time": extract_time,
                "decrypt_time": decrypt_time,
                "total_time": total_time,
                "final_size": len(decrypted_data)
            })

            print(f"  Файл успішно відновлено у '{output_file}'")

        except Exception as e:
            print(f"Сталася помилка: {e}")

    def show_analytics(self):
        print("\n--- Звіт ефективності --- \n")
        print(f"{'Операція':<15} | {'Час AES (с)':<12} | {'Час Stego (с)':<12} | {'Загальний час':<15} | {'Розмір (КБ)':<20}")
        print("-" * 85)
        
        for m in self.metrics:
            final_kb = m['final_size'] / 1024
            
            if m['operation'] == 'Захист':
                orig_kb = m['orig_size'] / 1024
                print(f"{m['operation']:<15} | {m['enc_time']:<12.4f} | {m['stego_time']:<12.4f} | {m['total_time']:<15.4f} | {orig_kb:.2f} -> {final_kb:.2f}")
            else:
                 print(f"{m['operation']:<15} | {m['decrypt_time']:<12.4f} | {m['extract_time']:<12.4f} | {m['total_time']:<15.4f} | {final_kb:.2f}")
        print("-" * 85)

    def run(self):
        while True:
            print("\n=== Комплексна система захисту (AES + LSB) ===")
            print("1. Захистити файл (Шифрування -> Приховування)")
            print("2. Відновити файл (Витягування -> Розшифрування)")
            print("3. Показати аналітику")
            print("4. Вихід")
            
            choice = input("Ваш вибір: ")
            
            if choice == '1':
                self.protect_process()
            elif choice == '2':
                self.restore_process()
            elif choice == '3':
                self.show_analytics()
            elif choice == '4':
                print("Роботу завершено")
                break
            else:
                print("Невірний вибір")

if __name__ == "__main__":
    app = SecuritySystem()
    app.run()