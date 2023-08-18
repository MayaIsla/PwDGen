import string    
import random 
N = 4   
L = 4
P = 1
A = 1

alpha = ''.join(random.choices( string.ascii_uppercase, k=A))
lower = ''.join(random.choices( string.ascii_lowercase, k=L))
num = ''.join(random.choices(string.digits, k=N))
punc = ''.join(random.choices(string.punctuation, k=P))

print(alpha + lower + num + punc)




#pwd = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation , k = S))    
#print(str(pwd)) 
