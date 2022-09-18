#Write Your Code Here
n=int(input())
if n==0:
    print(0);
else:
    ans=0;
    while n>0:
        digit=(int)(n%10);
        ans=ans*10+digit;
        n=n/10;
        
    print(ans);    
