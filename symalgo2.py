# Fernet module is imported from the
# cryptography package
from cryptography.fernet import Fernet


# key is generated
key = Fernet.generate_key()

# value of key is assigned to a variable
f = Fernet(key)

# the plaintext is converted to ciphertext
token = f.encrypt(b"PROGRAM IS CREATED BY SIDDHESH DAHATONDE")

# display the ciphertext
print("The cipher text is:")
print(token)

# decrypting the ciphertext
print("The decrypted text is:")
d = f.decrypt(token)

# display the plaintext and the decode() method
# converts it from byte to string
print(d.decode())
