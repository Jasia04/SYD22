# Read and print each line from the file, removing newline characters at the end
with open("raw_text.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes the newline character

# Encrypt a single character based on the custom rules
def encrypt_character(char, n, m):
    if char.islower():
        if 'a' <= char <= 'm':
            # Shift forward by n * m
            return chr((ord(char) - ord('a') + n * m) % 26 + ord('a'))
        elif 'n' <= char <= 'z':
            # Shift backward by n + m
            return chr((ord(char) - ord('a') - (n + m)) % 26 + ord('a'))
    elif char.isupper():
        if 'A' <= char <= 'M':
            # Shift backward by n
            return chr((ord(char) - ord('A') - n) % 26 + ord('A'))
        elif 'N' <= char <= 'Z':
            # Shift forward by m squared
            return chr((ord(char) - ord('A') + m**2) % 26 + ord('A'))
    else:
        return char  # Leave non-alphabet characters unchanged

# Decrypt a single character by reversing the encryption logic
def decrypt_character(char, n, m):
    if char.islower():
        if 'a' <= char <= 'm':
            # Reverse forward shift: subtract n * m
            return chr((ord(char) - ord('a') - n * m) % 26 + ord('a'))
        elif 'n' <= char <= 'z':
            # Reverse backward shift: add n + m
            return chr((ord(char) - ord('a') + (n + m)) % 26 + ord('a'))
    elif char.isupper():
        if 'A' <= char <= 'M':
            # Reverse backward shift: add n
            return chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        elif 'N' <= char <= 'Z':
            # Reverse forward shift: subtract m squared
            return chr((ord(char) - ord('A') - m**2) % 26 + ord('A'))
    else:
        return char  # Leave non-alphabet characters unchanged

# Encrypt the full text by applying encrypt_character to each character
def encrypt_text(text, n, m):
    return ''.join(encrypt_character(c, n, m) for c in text)

# Decrypt the full text by applying decrypt_character to each character
def decrypt_text(text, n, m):
    return ''.join(decrypt_character(c, n, m) for c in text)

# Compare the original and decrypted text for verification
def verify_decryption(original, decrypted):
    return original == decrypted

# Main function to run the full process
def main():
    # Take user inputs for encryption parameters
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))

    # Step 1: Read original text from raw_text.txt
    with open("raw_text.txt", "r") as f:
        original_text = f.read()

    # Step 2: Encrypt the original text
    encrypted = encrypt_text(original_text, n, m)

    # Step 3: Save the encrypted text to encrypted_text.txt
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted)

    # Step 4: Decrypt the encrypted text
    decrypted = decrypt_text(encrypted, n, m)

    # Step 5: Verify that the decrypted text matches the original
    print("Decryption is correct:", verify_decryption(original_text, decrypted))

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
