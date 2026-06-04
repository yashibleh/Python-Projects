import string
expression = input("Enter expression:\n")
allowed = "01234567890-=+*/.()"
if all(c in allowed for c in expression):
    number=""
    tokens=[]
    for c in expression:
        if c.isdigit():
            number+=c
    else:
        tokens.append(int(number))
        tokens.append(c)
        number=""
if number:
    tokens.append(int(number))