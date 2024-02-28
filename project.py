import streamlit as st
import string
import random

def generate_password(length, use_digits=True, use_letters=True, use_special=True):
    character_list = ""
    if use_digits:
        character_list += string.digits
    if use_letters:
        character_list += string.ascii_letters
    if use_special:
        character_list += string.punctuation
    if not (use_digits or use_letters or use_special):
        raise ValueError("At least one character set must be selected.")

    return ''.join(random.choices(character_list, k=length))

def main():
    st.title("Random Password Generator")

    length = st.number_input("Enter password length:", min_value=1, step=1, value=8)

    use_digits = st.checkbox("Include Digits (0-9)", value=True)
    use_letters = st.checkbox("Include Letters (A-Z, a-z)", value=True)
    use_special = st.checkbox("Include Special Characters", value=True)

    if st.button("Generate Password"):
        try:
            password = generate_password(length, use_digits, use_letters, use_special)
            st.success("Your random password is: " + password)
        except ValueError as ve:
            st.error("Error: " + str(ve))

if __name__ == "__main__":
    main()
