# code for Password Generator
import random
import string
def generate_password(length):
 characters = string.ascii_letters + string.digits + string.punctuation
 password = ''.join(random.choice(characters) for _ in range(length))
 return password
# Asking user name
user_name = input("Enter your name : ")
# Asking User the lenght of password
password_length = int(input("Enter the desired password length: "))
# printing the Generated password
generated_password = generate_password(password_length)
print("Generated password:", generated_password)