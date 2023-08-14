import string    
import random 
S = 10   
 
pwd = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation , k = S))    
print(str(pwd)) 