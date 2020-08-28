'''
A strong password needs following requiremments
1. Must be 8 chars
2. Atleast 1 uppercase letter
2. Atleast 1 lowercase letter
3. Atleast 1 number
4. Atleast 1 special char(!@#$)
We use lists of all these requirements to generate a random pwd
'''
import random
def pwd_generator():
    lowercase_chars=['a','b','c','d','e','f']
    uppercase_chars=['A','B','C','D','E','F']
    nums=['1','2','3','4','5','6','7','8','9']
    spl_chars=['!','@','#','$','&']
    password=random.choice(lowercase_chars)+random.choice(uppercase_chars)+random.choice(nums)+random.choice(spl_chars)
    pwd=password+password
    return pwd
print("The random password is \' {} \'".format(pwd_generator()))
