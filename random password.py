import random 

lower = "abcd"
uper = "ABCD"
numbers = "123456"
simbles = "!@#$%^*&"

string = lower + uper + numbers + simbles 
lenth = 10 
pasword = "".join(random.sample(string,lenth))

print("Your password is: ",pasword) 


