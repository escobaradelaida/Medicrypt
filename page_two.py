import tkinter as tk
import os
from cryptography.fernet import Fernet
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load the image using PIL
        self.bg_image = Image.open('medicrypt_HQ.png')
        self.bg_photo = controller.resize_image(self.bg_image, 800, 600)

        # Create a label to display the background image
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = tk.Label(self, text='This is page two', font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)

        button = tk.Button(self, text='Go to the Start Page', command=lambda: controller.show_frame('StartPage'))
        button.pack()

        # Label to show the selected encrypted file
        self.selected_label = tk.Label(self, text='', bg='gray')
        self.selected_label.pack()

        # Import button to import the encrypted file
        import_button = tk.Button(self, text='Import File...', command=self.import_encrypted_file)
        import_button.pack()

        # Label to show the selected key file
        self.key_label = tk.Label(self, text='', bg='gray')
        self.key_label.pack()

        # Button to import the key file
        import_key_button = tk.Button(self, text='Import Key File...', command=self.import_key_file)
        import_key_button.pack()

        # Decrypt button for user
        decrypt_button = tk.Button(self, text='Decrypt', command=self.decrypt_and_display)
        decrypt_button.pack()

        # Label to display decrypted file name
        self.decrypted_label = tk.Label(self, text='', bg='gray')
        self.decrypted_label.pack()

        # Image preview label
        self.image_label = tk.Label(self)
        self.image_label.pack()

        # Button to download the decrypted image
        download_button = tk.Button(self, text='Download Image', command=self.download_image)
        download_button.pack()

        # Ensure widgets appear above the background
        label.lift()
        button.lift()
        import_button.lift()
        import_key_button.lift()
        decrypt_button.lift()
        self.selected_label.lift()
        self.key_label.lift()
        self.decrypted_label.lift()
        self.image_label.lift()
        download_button.lift()

        # Store the selected encrypted file, key file, and decrypted image path
        self.selected_encrypted_file = None
        self.selected_key_file = None
        self.decrypted_filename = None

    # Method to select an encrypted file
    def import_encrypted_file(self):
        filename = filedialog.askopenfilename(title="Select a file", filetypes=[("All Files", "*.*")])
        if filename:
            self.selected_encrypted_file = filename
            self.selected_label.config(text=f"Selected file: {filename}")
            print("Selected file: ", filename)

    # Method to select a key file
    def import_key_file(self):
        filename = filedialog.askopenfilename(title="Select a key file", filetypes=[("Key Files", "*.key")])
        if filename:
            self.selected_key_file = filename
            self.key_label.config(text=f"Selected key file: {filename}")
            print("Selected key file: ", filename)

    # Decrypt and display the selected file
    def decrypt_and_display(self):
        if self.selected_encrypted_file and self.selected_key_file:
            # Decrypt the selected file using the selected key file
            decrypted_filename = self.decrypt_file(self.selected_encrypted_file, self.selected_key_file)
            if decrypted_filename:
                # Show the decrypted file name
                self.decrypted_label.config(text=f"Decrypted file: {decrypted_filename}")
                print("Decrypted file: ", decrypted_filename)

                # Display the decrypted image
                decrypted_image = Image.open(decrypted_filename)
                resized_image = decrypted_image.resize((800, 600), Image.LANCZOS)
                self.preview_image = ImageTk.PhotoImage(resized_image)
                self.image_label.config(image=self.preview_image)
                self.decrypted_filename = decrypted_filename
            else:
                print("Decryption failed.")
        else:
            if not self.selected_key_file:
                print("No key file selected")
            if not self.selected_encrypted_file:
                print("No encrypted file selected")

    # Method to decrypt the selected file using the selected key file
    def decrypt_file(self, encrypted_file, key_file):
        try:
            # Read the key from the selected key file
            with open(key_file, 'rb') as f:
                key = f.read()

            # Read the encrypted data
            with open(encrypted_file, 'rb') as f:
                encrypted_data = f.read()

            # Decrypt the data
            cipher = Fernet(key)
            decrypted_data = cipher.decrypt(encrypted_data)

            # Write the decrypted data to a new file
            decrypted_filename = os.path.splitext(encrypted_file)[0] + '_decrypted.png'
            with open(decrypted_filename, 'wb') as f:
                f.write(decrypted_data)

            return decrypted_filename

        except Exception as e:
            print(f"Error decrypting file: {e}")
            return None

    # Method to allow the user to download the displayed image
    def download_image(self):
        if self.decrypted_filename:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if save_path:
                try:
                    with open(self.decrypted_filename, 'rb') as f_src:
                        with open(save_path, 'wb') as f_dest:
                            f_dest.write(f_src.read())
                    messagebox.showinfo("Success", f"File saved as {save_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save file: {e}")
        else:
            messagebox.showwarning("Warning", "No decrypted file to save")

