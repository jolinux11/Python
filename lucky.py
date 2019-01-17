import random
import string
count=0
while count<4:
    x=random.randint(1,4)
    y=input('enetr any no betwen 1-20:')
    if (y==x):
        print ('lucky winner')
        break;
    else:
        print ('unlucky')
    count+=1
print ('lucky no is:',x)
