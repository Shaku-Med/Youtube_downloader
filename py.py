import hashlib

# Prompt the user for a password
password = input('Enter your password: ')

# Create a SHA-256 hash object
hash_object = hashlib.sha256()

# Update the hash object with the password
hash_object.update(password.encode())

# Get the hashed password
hashed_password = hash_object.hexdigest()

# Print the hashed password
print(f'Hashed password: {hashed_password}')