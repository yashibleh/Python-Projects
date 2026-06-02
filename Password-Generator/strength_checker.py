import string
def check_strength(pw):
    score=0
    if len(pw)>=8:
        score+=1
    if len(pw)>=12:
        score+=1
    if any(c.islower() for c in pw):
        score+=1
    if any(c.isupper() for c in pw):
        score+=1
    if any(c.isdigit() for c in pw):
        score+=1
    if any(c in string.punctuation for c in pw):
        score+=1
    if score<=2:
        return "Strength: Weak"
    elif score<=4:
        return "Strength: Medium"
    else:
        return "Strength: Strong"