import hashlib

# Ścieżki do plików
input_file = 'hasla.txt'  # Plik wejściowy z hasłami
output_file = 'hasla_md5.txt'  # Plik wyjściowy z hashami MD5

# Funkcja do hashowania hasła za pomocą MD5
def hash_md5(password):
    # Upewnij się, że hasło jest typu bytes
    if isinstance(password, str):
        password = password.encode('utf-8')
    # Tworzenie obiektu hashującego MD5
    md5_hash = hashlib.md5()
    # Aktualizacja obiektu hashującego o dane
    md5_hash.update(password)
    # Zwrócenie hasha w formie szesnastkowej
    return md5_hash.hexdigest()

# Otwieranie pliku wejściowego i wyjściowego
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # Iteracja przez każdą linię w pliku wejściowym
    for line in infile:
        # Usunięcie białych znaków (np. znaków nowej linii) z końca linii
        password = line.strip()
        # Pominięcie pustych linii
        if not password:
            continue
        # Hashowanie hasła
        hashed_password = hash_md5(password)
        # Zapisanie oryginalnego hasła i jego hasha do pliku wyjściowego
        outfile.write(f'{password} -> {hashed_password}\n')

print(f'Hashowanie zakończone. Wyniki zapisano w pliku {output_file}.')
