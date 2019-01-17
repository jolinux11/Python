import time
s='bottles of beer on the wall take one down and pass it around'

list1=[1]
count=0
while count<98:
    list1.append(list1[count]+1)
    count+=1
list1.reverse()

print '.................LETS PLAY THE GAME 99 BOTTLES OF BEER ON THE WALL...............'
time.sleep(1)
print '3'
time.sleep(1)
print '2'
time.sleep(1)
print '1','and','go\n'

count1=0
while count1<99:
    test=[]
    test=list1[count1]
    print test
    print s
    time.sleep(2)
    count1+=1
