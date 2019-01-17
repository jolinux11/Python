import math
def circle_area(var):
    area =math.pi*var**2
    return area
def circle_circumerence(var):
    ans=2*math.pi*var
    return ans
def cap_str(test):
    return test.upper()
x=input('eneter 1 for area of circle 2 for circumference of circle 3 for operation on string 4 for exit:')

if x==1:
    var=input('enter radius:')
    test1=circle_area(var)
    print ('area of circle:',test1)
elif x==2:
    var=input('enter radius:')
    test2=circle_circumference(var)
    print ('circumference of circle:',test2)
elif x==3:
    test=input('enter string:')
    test3=cap_str(test)
    print ('uppercase of string:',test3)
else:
    exit()
