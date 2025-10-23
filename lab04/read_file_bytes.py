import sys

def read_file_bytes(filepath):

    try:
        with open(filepath, 'rb') as f:
            file_bytes = f.read()
        return file_bytes
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом: {filepath}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Помилка читання файлу: {e}", file=sys.stderr)
        return None