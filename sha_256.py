import hashlib

# Ścieżki do plików
input_file = 'hasla.txt'  # Plik wejściowy z hasłami
output_file = 'hasla_sha256.txt'  # Plik wyjściowy z hashami SHA-256

# Funkcja do hashowania hasła za pomocą SHA-256
def hash_sha256(password):
    # Upewnij się, że hasło jest typu bytes
    if isinstance(password, str):
        password = password.encode('utf-8')
    # Tworzenie obiektu hashującego SHA-256
    sha256_hash = hashlib.sha256()
    # Aktualizacja obiektu hashującego o dane
    sha256_hash.update(password)
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
        # Hashowanie hasła
        hashed_password = hash_sha256(password)
        # Zapisanie oryginalnego hasła i jego hasha do pliku wyjściowego
        outfile.write(f'{password} -> {hashed_password}\n')

print(f'Hashowanie zakończone. Wyniki zapisano w pliku {output_file}.')
