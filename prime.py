n=input('Enter any num:')
flag=True
count=2
while count < n:
    if n % count == 0:
        flag=False
    count+=1
if flag == True:
    print ('n is prime num')
else:
    print ('n is not prime num')
