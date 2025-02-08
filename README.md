# SecureEncrypt

## Overview

**SecureEncrypt** is a Python-based project demonstrating the use of AES (Advanced Encryption Standard) and DES (Data Encryption Standard) encryption algorithms to secure data. This project leverages the `pycryptodome` library to provide robust encryption and decryption functionalities.
 

## Features

- **AES Encryption and Decryption**: Encrypts and decrypts data using AES algorithm.
- **DES Encryption and Decryption**: Encrypts and decrypts data using DES algorithm.
- **Automatic Algorithm Selection**: Selects the appropriate encryption algorithm based on the data size.
- **Data Padding**: Pads the data to match the block size for AES and DES algorithms.

## Installation

To run this project, you need to have Python 3.x installed. You also need the `pycryptodome` library, which you can install using pip.

### Prerequisites

- Python 3.x

### Installing `pycryptodome`

```bash
pip install pycryptodome
```

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/SecureEncrypt.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd SecureEncrypt
    ```

3. **Run the script:**

    ```bash
    python code.py
    ```

## Code Description

The main script `code.py` includes functions for AES and DES encryption and decryption. It also contains logic to select the appropriate encryption algorithm based on the size of the data. Here is a brief description of the main components:

### AES Encryption and Decryption Functions

- `encrypt_aes(data, key)`: Encrypts data using the AES encryption algorithm.
- `decrypt_aes(ciphertext, key)`: Decrypts AES-encrypted data.

### DES Encryption and Decryption Functions

- `encrypt_des(data, key)`: Encrypts data using the DES encryption algorithm.
- `decrypt_des(ciphertext, key)`: Decrypts DES-encrypted data.

### Algorithm Selection

- `select_algorithm(data)`: Selects the appropriate encryption algorithm based on the data size.

### Data Padding

- `pad_data(data, block_size)`: Pads the data to match the block size for AES and DES algorithms.

### Perform Encryption and Decryption

- `perform_encryption_decryption(data, algorithm)`: Handles the encryption and decryption process based on the selected algorithm.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


