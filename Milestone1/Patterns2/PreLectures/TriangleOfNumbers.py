from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.


n=int(input());

i=1;
while(i<=n):
   spaces=n-i; 
   while(spaces>0):
        print(" ",end="");
        spaces-=1;
   x=i;
   nos=1;
   while(nos<=i):
        print(x,end="");
        x+=1;
        nos+=1;
   y=i-1;
   z=x-2;
   while(y>0):
       print(z,end="");
       z-=1;
       y-=1; 
   print();
   i+=1;        














