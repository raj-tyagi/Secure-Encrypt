!pip install pycryptodome


from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
import base64
import hashlib

# AES Encryption and Decryption Functions
def encrypt_aes(data, key):
    """
    Encrypts data using AES encryption algorithm.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    ct_bytes = cipher.encrypt(data)
    return base64.b64encode(ct_bytes)

def decrypt_aes(ciphertext, key):
    """
    Decrypts AES-encrypted data.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    ct_bytes = base64.b64decode(ciphertext)
    return cipher.decrypt(ct_bytes).decode('utf-8')

# DES Encryption and Decryption Functions
def encrypt_des(data, key):
    """
    Encrypts data using DES encryption algorithm.
    """
    cipher = DES.new(key, DES.MODE_ECB)
    ct_bytes = cipher.encrypt(data)
    return base64.b64encode(ct_bytes)

def decrypt_des(ciphertext, key):
    """
    Decrypts DES-encrypted data.
    """
    cipher = DES.new(key, DES.MODE_ECB)
    ct_bytes = base64.b64decode(ciphertext)
    return cipher.decrypt(ct_bytes).decode('utf-8')

# Function to select encryption algorithm based on various factors
def select_algorithm(data):
    security_threshold = {
        "DES": 8,   # Consider DES for small data (< 8 bytes)
        "AES": 256, # Consider AES for data up to 256 bytes
    }

    # Considerations based on data size
    if len(data) < security_threshold["DES"]:
        return "DES"
    elif len(data) <= security_threshold["AES"]:
        return "AES"

# Function to pad data to match the block size
# (Pad data for DES and AES block size)
def pad_data(data, block_size):
    pad_length = block_size - len(data) % block_size
    padding = bytes([pad_length]) * pad_length
    return data + padding if pad_length != block_size else data

# Function to handle encryption and decryption based on selected algorithm
def perform_encryption_decryption(data, algorithm):
    encrypted = ""
    decrypted = ""
    key_information = ""

    if algorithm == "AES":
        key = get_random_bytes(16)
        padded_data = pad_data(data.encode('utf-8'), 16)
        encrypted = encrypt_aes(padded_data, key)
        decrypted = decrypt_aes(encrypted, key)
        key_information = f"AES Key (MD5 Hash): {hashlib.md5(key).hexdigest()}"
    elif algorithm == "DES":
        key = get_random_bytes(8)
        padded_data = pad_data(data.encode('utf-8'), 8)
        encrypted = encrypt_des(padded_data, key)
        decrypted = decrypt_des(encrypted, key)
        key_information = f"DES Key (MD5 Hash): {hashlib.md5(key).hexdigest()}"

    return encrypted, decrypted, key_information

# User input
input_data = input("Enter the data to encrypt: ")

# Select algorithm based on various factors
selected_algorithm = select_algorithm(input_data)

# Perform encryption and decryption
encrypted_data, decrypted_data, key_information = perform_encryption_decryption(input_data, selected_algorithm)

# Display results
print(f"Selected Algorithm: {selected_algorithm}")
print(f"Key Information: {key_information}")
print(f"Encrypted Data: {encrypted_data}")
print(f"Decrypted Data: {decrypted_data}")
