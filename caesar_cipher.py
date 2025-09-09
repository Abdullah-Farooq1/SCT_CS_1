# Caesar Cipher Program

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift letters
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep spaces/punctuation unchanged
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)  # Just reverse the shift


# Main program
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted_text = encrypt(message, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print(f"\nEncrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")
