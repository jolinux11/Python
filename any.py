a,b=0,1
d=[]
d.append(a)
d.append(b)
count=0
c=[]
while count <20:
    c=a+b
    d.append(c)
    a=b
    b=c
    count+=1
print ('d:',d)
