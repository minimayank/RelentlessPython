
num = int(input());
rev=0;
while (num>0):
    
    rev=rev*10+num%10;
    num=num//10;
#Implement Your Code Here
   
if(rev==num):
    print("true");
else:
    print("false");   
#ERRORR
