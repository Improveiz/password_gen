import random
import string

length = int(input('Enter length of password: '))

letters = string.ascii_letters
numb = string.digits
punc = string.punctuation

all = letters+numb+punc

temp = random.sample(all,length)

password = ''.join(temp)

print(password)