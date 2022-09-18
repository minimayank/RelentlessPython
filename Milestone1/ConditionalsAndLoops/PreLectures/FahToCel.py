# Read input as sepcified in the question
# Print output as specified in the question

start=int(input())
end=int(input())
stepSize=int(input())

while start<=end:
    temp=start-32
    celsius=(int)((temp*5)/9)
    print(str(start)+" "+str(celsius))
    start=start+stepSize
