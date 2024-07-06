import re
regex=re.compile("^[a-z_.A-Z0-9]*\@[a-z_.A-Z]*\.[a-z]{2,}$")
chaine="salahbk44@gmail.com"
p=regex.match(chaine)
if p is not None:
    print("valid")
else:
    print("non valide")