import random
import string
print('..............WELLCOME TO LUCKY DRAW COMPETITION....................')
list1=string.printable
list1.remove(1)
list1.remove(1)
def my_input():
    w=input('press 1 to start game press 0 to exit:')
    return w

myinput=my_input()
if myinput==1:
    
    test=random.randint(1,20)
    print test

    count=0
    while count<4:
        x=input('enter any no from 1-20:')

        if x==test:
            print 'lucky winner'

            if count==0:
                print 'you win fridge'
            elif count==1:
                print 'you win tv'
            elif count==2:
                print 'you win mobile'
            else:
                print 'you win pendrive'
            break;
        else:
            print ('unlucky')
            if x<test:
                print 'NOTE:Number is smaller than guess','Enter bigger number'
            else:
                print 'NOTE:Number is larger than guess','Enter smaller number'
        count+=1
        if count==4:
            print 'hard luck'


elif myinput==0:
    exit()
else:
    myinput==list1
    print 'Enter correct input'
    my_input()

#if count==4:
#    print 'lucky num is:',test

