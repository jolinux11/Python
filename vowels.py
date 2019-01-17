test123= input('enter required string:')
test_str=[]

var=0
while var< len(test123):
    test_str.append(test123[var])
    var+=1
print test_str

list2=[]
count=0
count1=0
count2=0
count3=0
count4=0

vow=['a','e','i','o','u']

while count<10:
    if 'a' in test_str:
        test1=test_str.index('a')
        list1=test_str.pop(test1)
        list2.append(list1)

    else:
        break;


while count<10:
    if 'e' in test_str:
        test1=test_str.index('e')
        list1=test_str.pop(test1)
        list2.append(list1)

    else:
        break;

while count<10:
    if 'i' in test_str:
        test1=test_str.index('i')
        list1=test_str.pop(test1)
        list2.append(list1)

    else:
        break;

while count<10:
    if 'o' in test_str:
        test1=test_str.index('o')
        list1=test_str.pop(test1)
        list2.append(list1)

    else:
        break;

while count<10:
    if 'u' in test_str:
        test1=test_str.index('u')
        list1=test_str.pop(test1)
        list2.append(list1)

    else:
        break;


print 'vowels:' ,list2
print 'string:' ,test_str
