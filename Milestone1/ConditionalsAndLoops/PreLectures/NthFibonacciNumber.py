## Read input as specified in the question.
## Print output as specified in the question.


def fib(n):
    first=1;
    second=1;
    if n==1:
        return 1;
    if n==2:
        return 1;
    i=3;
    ans=1;
    while i<=n:
        ans=first+second;
        first=second;
        second=ans;
        i+=1;
    return ans;    
    
n=int(input());    
print(fib(n));    
