from tkinter import *
from tkinter import filedialog, messagebox


def encrypt_image():
    file = filedialog.askopenfile(mode='rb', filetypes=[('Image Files', '*.jpg')])
    if file is not None:
        filename = file.name
        key = entry1.get("1.0", END).strip()
        if not key.isdigit():
            messagebox.showerror("Invalid Key", "Key must be a numeric value.")
            return
        key = int(key)
        try:
            with open(filename, 'rb') as f:
                image = bytearray(f.read())

            for index, value in enumerate(image):
                image[index] = value ^ key

            with open(filename, 'wb') as f:
                f.write(image)

            messagebox.showinfo("Success", "Image encrypted/decrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


root = Tk()
root.geometry("250x120")
root.title("Image Encryptor/Decryptor")

b1 = Button(root, text="Encrypt/Decrypt", command=encrypt_image)
b1.pack(pady=10)

entry1 = Text(root, height=1, width=10)
entry1.pack(pady=10)

root.mainloop()
