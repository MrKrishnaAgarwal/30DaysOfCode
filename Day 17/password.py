import random as r
import string as s

password=s.ascii_letters+s.digits+s.punctuation+s.ascii_lowercase+s.ascii_uppercase+s.ascii_letters
password=''.join(r.sample(password,10))
print("The randomly generated password is:", password)
