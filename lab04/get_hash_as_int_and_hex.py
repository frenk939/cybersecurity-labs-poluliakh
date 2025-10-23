import sys
import hashlib

MODULUS = 1000007

def get_hash_as_int_and_hex(data_bytes):

    try:
        sha256 = hashlib.sha256()
        sha256.update(data_bytes)
        hex_hash = sha256.hexdigest()
        int_hash = int(hex_hash, 16) % MODULUS
        return int_hash, hex_hash
    except Exception as e:
        print(f"[Помилка хешування]: {e}", file=sys.stderr)
        return 0, "ERROR"