from numpy import random

i = 0
b = "abcdefghijklmnopqrstuvwxyz"
a = b.upper()
c = "\\!@#$%^&*()_+-=}{|:><?[];/.,|"
d = ""
while i < 24:
 x = random.randint(9)
 y = random.randint(25)
 z = random.randint(25)
 t = random.randint(25)
 d = f"{d}{x}{a[z]}{b[y]}{c[t]}"
 i = i+1
d = list(d)
random.shuffle(d)
print("key ",''.join(d))
input("Press Enter to exit...")
