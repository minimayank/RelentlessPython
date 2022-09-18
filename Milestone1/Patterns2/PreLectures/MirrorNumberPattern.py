## Read input as specified in the question
## Print the required output in given format

i=1;
n=int(input());
while(i<=n):
    spaces=n-i;
    j=spaces+1;
    while(spaces>0):
        print(" ",end="");
        spaces-=1;
    
    k=1;
    while(j<=n):
        print(k,end="");
        k+=1;
        j+=1;
    print();
    i+=1;    
    
