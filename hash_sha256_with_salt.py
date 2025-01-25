import hashlib
import os

# Ścieżki do plików
input_file = 'hasla.txt'  # Plik wejściowy z hasłami
output_file = 'hasla_sha256_salted.txt'  # Plik wyjściowy z hasłami i ich hashami

# Funkcja do generowania soli
def generate_salt():
    # Generowanie 16-bajtowej soli
    return os.urandom(16)

# Funkcja do hashowania hasła z solą za pomocą SHA-256
def hash_password(password, salt):
    # Upewnij się, że hasło jest typu bytes
    if isinstance(password, str):
        password = password.encode('utf-8')
    # Połączenie hasła i soli
    password_salt = password + salt
    # Tworzenie obiektu hashującego SHA-256
    sha256_hash = hashlib.sha256()
    # Aktualizacja obiektu hashującego o dane
    sha256_hash.update(password_salt)
    # Zwrócenie hasha w formie szesnastkowej
    return sha256_hash.hexdigest()

# Otwieranie pliku wejściowego i wyjściowego
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # Iteracja przez każdą linię w pliku wejściowym
    for line in infile:
        # Usunięcie białych znaków (np. znaków nowej linii) z końca linii
        password = line.strip()
        # Pominięcie pustych linii
        if not password:
            continue
        # Generowanie unikalnej soli dla każdego hasła
        salt = generate_salt()
        # Hashowanie hasła z solą
        hashed_password = hash_password(password, salt)
        # Zapisanie oryginalnego hasła, soli i jego hasha do pliku wyjściowego
        # Zapisujemy sól w formie szesnastkowej, aby była czytelna
        outfile.write(f'{password} -> Salt: {salt.hex()} -> Hash: {hashed_password}\n')

print(f'Hashowanie zakończone. Wyniki zapisano w pliku {output_file}.')
