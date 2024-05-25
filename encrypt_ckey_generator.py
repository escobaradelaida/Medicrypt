# creating a class to encrypt an image

from cryptography.fernet import Fernet

encrypted_key = Fernet.generate_key()

with open('key.key', 'wb') as f:
    f.write(encrypted_key)

print("Encryption key has been generated and saved in key.key file.")

# i would like to create a new scene in the guy with this function as a button