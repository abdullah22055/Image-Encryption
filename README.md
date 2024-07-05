# Image Encryptor/Decryptor

A simple GUI-based application to encrypt and decrypt images using XOR encryption. This project is built using Python and Tkinter.

## Features

- Encrypt or decrypt any `.jpg` image file.
- Simple and intuitive GUI for ease of use.
- XOR encryption with a user-provided numeric key.

## Requirements

- Python 3.12
- Tkinter library (usually included with Python installations)

## Installation

1. **Clone the repository**:
    
    git clone https://github.com/your-username/image-encryptor.git
    cd image-encryptor
    

2. **Install necessary dependencies**:
    No additional dependencies are required apart from Tkinter, which is included in most Python installations.

## Usage

1. **Run the application**:
    
    python encryptor.py
    

2. **Encrypt/Decrypt an Image**:
    - Click the "Encrypt/Decrypt" button.
    - Select a `.jpg` image file to encrypt or decrypt.
    - Enter a numeric key in the text box.
    - The selected image will be encrypted or decrypted based on the provided key.

## Example

1. **Start the application**:
    ![App Screenshot](screenshots/app.png)

2. **Select an image and enter the key**:
    ![Key Entry](screenshots/key_entry.png)

3. **Encrypted/Decrypted image saved**:
    ![Success Message](screenshots/success.png)

## How It Works

The application uses XOR encryption to modify the bytes of the selected image file. Each byte of the image is XORed with the provided key, and the resulting byte array is saved back to the original file.


## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

## Acknowledgments

- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)

