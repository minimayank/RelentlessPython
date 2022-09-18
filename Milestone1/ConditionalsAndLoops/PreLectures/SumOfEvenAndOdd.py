## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
odd=0;
even=0;
n=int(input())
if(n==0):
    print(0);
else:
    
    while(n>0):
        if(n%2==0):
            even+=n%10;
        else:
            odd+=n%10;
            
        n=n//10; 
        
        
print(even," ",odd);
