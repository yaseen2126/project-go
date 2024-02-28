import streamlit as st
import random
import string

st.title("Bano Qabil")

st.sidebar.markdown("""
    <div style="display: flex; justify-content: center;">
        <img src="https://banoqabil.pk/media/logo.png" width="200">
    </div>
""", unsafe_allow_html=True)

def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    st.sidebar.title("Navigation")
    tab = st.sidebar.radio("", ["Home", "About us", "Contact us"])

    if tab == "Home":
        st.title("Password Generator")
        length = st.slider("Select password length", 6, 30, 12)
        use_uppercase = st.checkbox("Include Uppercase Letters")
        use_numbers = st.checkbox("Include Numbers")
        use_special = st.checkbox("Include Special Characters")

        if st.button("Generate Password"):
            password = generate_password(length, use_uppercase, use_numbers, use_special)
            st.success("Your generated password is:")
            st.write(password)
    elif tab == "About us":
        st.title("About Us")
        
    elif tab == "Contact us":
        st.title("Contact Us")
        st.write("Email: www.yaseenkhan2126@gmail.com")

if __name__ == "__main__":
    main()
