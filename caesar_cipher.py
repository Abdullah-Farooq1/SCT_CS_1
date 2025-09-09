def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    try:
        message = input("Enter your message: ")
        shift_input = input("Enter shift value (integer): ")
        shift = int(shift_input)
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        exit(1)

    encrypted_text = encrypt(message, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print(f"\nOriginal: {message}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")
