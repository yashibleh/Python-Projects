import random
import string
pwlength = int(input("Enter required length of password(minimum 4):\n"))
if pwlength<4:
    print("Password length needs to be atleast 4")
else:
    pw=[
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    left = pwlength - 4

    all_charac = (string.ascii_letters + string.digits + string.punctuation)

    for x in range(left):
        pw.append(random.choice(all_charac))

    random.shuffle(pw)
passw = "".join(pw)
print("Generated password: ","".join(pw))
