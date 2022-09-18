def area(a,b):
    return a*b;

x1=int(input());
y1=int(input());
x2=int(input());
y2=int(input());
a=x2-x1;
if(a<0):
    a=-1*a;

b=y2-y1;
if(b<0):
    b=-1*b;
    
print(area(a,b));
