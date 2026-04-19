import string


def sprawdz_bezpieczenstwo(haslo):

    if len(haslo) <= 8:
        return False
    
    znaki_hasla = set(haslo)

    ma_male = not znaki_hasla.isdisjoint(string.ascii_lowercase)
    ma_duze = not znaki_hasla.isdisjoint(string.ascii_uppercase)
    ma_cyfry = not znaki_hasla.isdisjoint(string.digits)
    ma_znaki = not znaki_hasla.isdisjoint(string.punctuation)

    return ma_male and ma_duze and ma_cyfry and ma_znaki

print(sprawdz_bezpieczenstwo("Slabe1!"))
print(sprawdz_bezpieczenstwo("DobreHaslo1!"))