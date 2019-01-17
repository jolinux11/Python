def myinput():
    x=input('enter 1 or 0:')
    return x
my_input=myinput()
count=0
while count<5:
    if my_input==1:
        print 'sucess'
        break;
    elif my_input==0:
        print 'defeat'
        exit()
    else:
        myinput()
    count+=1
