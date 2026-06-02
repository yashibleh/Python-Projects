import random
import string

pwlength = int(input("Enter required length of password (minimum 4): "))

if pwlength < 4:
    print("Password length needs to be at least 4")

else:
    opt = input("Do you want to include numbers? (Y/N): ")
    opt2 = input("Do you want to include symbols? (Y/N): ")
    characters = string.ascii_letters

    if opt == "Y" or opt == "y":
        characters += string.digits

    if opt2 == "Y" or opt == "y":
        characters += string.punctuation

    password = []

    # Ensure at least one lowercase and one uppercase
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))

    if opt == "Y" or opt == "y":
        password.append(random.choice(string.digits))

    if opt2 == "Y" or opt2 == "y":
        password.append(random.choice(string.punctuation))

    while len(password) < pwlength:
        password.append(random.choice(characters))

    random.shuffle(password)

    print("Generated password:", "".join(password))