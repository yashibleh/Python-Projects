import random
import string
from strength_checker import check_strength
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

    pw = []
    pw.append(random.choice(string.ascii_lowercase))
    pw.append(random.choice(string.ascii_uppercase))

    if opt == "Y" or opt == "y":
        pw.append(random.choice(string.digits))

    if opt2 == "Y" or opt2 == "y":
        pw.append(random.choice(string.punctuation))

    while len(pw) < pwlength:
        pw.append(random.choice(characters))

    random.shuffle(pw)

    print("Generated password:", "".join(pw))
    print(check_strength(pw))