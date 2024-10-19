from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key) # Stored as bytes

message = b'This is my secret message!'

engine = Fernet(key)

print(engine.encrypt(message))

