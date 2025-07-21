def letter_positions(text):
    text = text.lower()  # make everything lowercase for consistency
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in text:
        if char in alphabet:
            position = alphabet.index(char) + 1  # +1 because index starts at 0
            print(f"'{char.upper()}' is at position {position}")
        else:
            print(f"'{char}' is not a letter, skipped.")

# Ask for user input
user_input = input("Enter some text: ")
letter_positions(user_input)

