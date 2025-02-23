alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter  # Keep spaces, punctuation, and numbers unchanged

    print(f"Encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    output_text = ""

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter  # Keep spaces, punctuation, and numbers unchanged

    print(f"Decoded result: {output_text}")

# Loop for multiple operations
while True:
    direction = input("\nType 'encode' to encrypt, 'decode' to decrypt, or 'exit' to quit:\n").lower()

    if direction == "exit":
        print("Goodbye! 👋")
        break

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift)
    else:
        print("Invalid input! Please type 'encode', 'decode', or 'exit'.")
