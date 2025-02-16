import streamlit as st
import random
import string
import json
import os
from datetime import datetime

def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    """Generate a random password based on specified criteria"""
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "Please select at least one character type"
    
    return ''.join(random.choice(characters) for _ in range(length))

def save_credentials(username, password):
    """Save username and password to a JSON file"""
    data = {
        'username': username,
        'password': password,
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Load existing credentials
    credentials = []
    if os.path.exists('credentials.json'):
        with open('credentials.json', 'r') as f:
            credentials = json.load(f)
    
    # Add new credentials
    credentials.append(data)
    
    # Save updated credentials
    with open('credentials.json', 'w') as f:
        json.dump(credentials, f, indent=4)

def load_credentials():
    """Load saved credentials from JSON file"""
    if os.path.exists('credentials.json'):
        with open('credentials.json', 'r') as f:
            return json.load(f)
    return []

# Set page config
st.set_page_config(page_title="Password Generator & Manager", layout="wide")

# Add title and description
st.title("Password Generator & Manager")
st.write("Generate secure passwords and store your credentials safely.")

# Create tabs for different functionalities
tab1, tab2 = st.tabs(["Generate Password", "View Saved Credentials"])

with tab1:
    st.header("Generate New Password")
    
    # Password generation options
    col1, col2 = st.columns(2)
    
    with col1:
        password_length = st.slider("Password Length", 8, 32, 12)
        use_letters = st.checkbox("Include Letters", value=True)
        use_numbers = st.checkbox("Include Numbers", value=True)
        use_symbols = st.checkbox("Include Symbols", value=True)
    
    with col2:
        if st.button("Generate Password"):
            generated_password = generate_password(
                password_length,
                use_letters,
                use_numbers,
                use_symbols
            )
            st.session_state['generated_password'] = generated_password
            st.code(generated_password)
    
    # Save credentials section
    st.header("Save Credentials")
    
    username = st.text_input("Username")
    password = st.text_input("Password", value=st.session_state.get('generated_password', ''))
    
    if st.button("Save Credentials"):
        if username and password:
            save_credentials(username, password)
            st.success("Credentials saved successfully!")
        else:
            st.error("Please enter both username and password")

with tab2:
    st.header("Saved Credentials")
    
    # Load and display saved credentials
    credentials = load_credentials()
    
    if credentials:
        for cred in credentials:
            with st.expander(f"Username: {cred['username']} (Created: {cred['created_at']})"):
                st.text(f"Password: {cred['password']}")
    else:
        st.info("No saved credentials found")

# Add safety information
st.sidebar.title("Security Notice")
st.sidebar.warning("""
This is a demonstration app. In a production environment:
- Passwords should be encrypted
- Use secure storage methods
- Implement proper user authentication
- Add additional security measures
""")