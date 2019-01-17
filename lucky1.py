import random
import string

test=random.randint(1,20)
#print test
count=0
while count<4:
    x=input('enter any no from 1-20:')

    if x==test:
        print 'lucky winner'
        break;
    else:
        print ('unlucky')
    count+=1
    if count==4:
        print 'hard luck'
print 'lucky num is:',test
