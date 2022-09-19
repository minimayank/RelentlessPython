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
i=0;
stars=1;
while i<n:
    spaces=n-i-1;
    while spaces>0:
        print(" ",end="");
        spaces-=1;
    stars=1+2*i;
    while stars>0:
        print("*",end="");
        stars-=1;
    print();    
    i+=1;
    
    
    
    
