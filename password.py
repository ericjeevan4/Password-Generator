import streamlit as st
import random
import string
import pyperclip

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    st.title("Advanced Password Generator")
    
    st.sidebar.subheader("Password Complexity Options")
    length = st.sidebar.slider("Password Length", 8, 32, 12)
    include_uppercase = st.sidebar.checkbox("Include Uppercase Letters", value=True)
    include_numbers = st.sidebar.checkbox("Include Numbers", value=True)
    include_symbols = st.sidebar.checkbox("Include Symbols", value=True)
    
    if st.button("Generate Password"):
        password = generate_password(length, include_uppercase, include_numbers, include_symbols)
        st.success(f"Generated Password: {password}")
        pyperclip.copy(password)
        st.info("Password copied to clipboard!")
    
if __name__ == "__main__":
    main()
