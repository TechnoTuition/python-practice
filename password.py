import random
import string

class Password:
    def __init__(self,num):
        self.num = num
    def passGen(self,num):
        x = list(string.ascii_letters + string.digits + string.punctuation)
        random.shuffle(x)
        a = "".join(x)[0:self.num]
        return a
        
passg = Password(int(input("number: "))) 
print(passg.passGen(10))