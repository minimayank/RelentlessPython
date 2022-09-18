## Read input as specified in the question
## Print the required output in given format
def pattern(n):
    i=1;
    while i<=n:
        num=i;
        j=0;
        while j<i:
            print(num,end="");
            j+=1;
        print(); 
        i+=1;

num=int(input());
pattern(num);
