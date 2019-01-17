product={1:'cpu',2:'monitor',3:'mouse',4:'keyboard',5:'ram',6:'nic',7:'usb',8:'hdd',9:'speaker',10:'smps'}
price={1:10000,2:3000,3:199,4:299,5:3499,6:699,7:499,8:3700,9:1500,10:1500}
cart=[]
bill=[]
count=0
total=0
addition=[]
c=[]
x=0
while count < 100:
    n=input("To add product to the cart press 1 or press 0 to exit:")
    if n ==1:
        print (product)
        m=input('Enter the product code:')
        cart.append(m)
        c.append(price[m])
        print (c)
    else:
        print ('shoping done wait for billing')
        while x < len(c):
                total=total+c[x]
                x+=1
        break;
bill=((total*118)/100)
print ('Total cart items:',cart)
print ('TOTAL BILL AMOUNT FOR PURCHASE INCLUDING 18 % GST:',bill)
