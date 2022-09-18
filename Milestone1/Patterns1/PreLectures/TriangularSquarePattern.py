## Read input as specified in the question
## Print the required output in given format

def pattern(x):
    i=0;
    while i<x:
        j=0;
        while j<=i:
            print("*",end="");
            j+=1;
        print();
        i+=1;
        
n=int(input());
pattern(n);
            
