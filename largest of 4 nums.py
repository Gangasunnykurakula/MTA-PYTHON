#Largest of 4 numbers
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if(a>=b and a>=c and a>=d):
    print(a,'A is greater')
elif(b>=c and b>=d):
    print(b,'B is greater')
elif(c>=d):
    print(c,'C is greater')
else:
    print(d,'D is greater')
