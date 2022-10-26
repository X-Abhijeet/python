print("good morning🐟")

if 1>2:
    print("true")
else:
    print("false")


a=2
A=2
b=A+a
print(b)
value=(1+1)*2**4//3+4-1
print(value)
a=5
b=2
c=a/b
print(c)
print(type(c))
x=2.5
y=3.5 
z=x+y
print(z)
print(type(z))
p="X_"# string is written under double cot
q="Abhijeet"
r=p+q
print(r)
print(type(r))
a=5
b=2
c=a/b
d=int(c)
print(d)
print(type(d))
p=10
q="20"
r=p+int(q)
print(r)
n="Abhijeet"
vn=tuple(n)
print(vn)
print(type(vn))
n= ("ram", "shyam","mohan","sohan")
vn=list(n)
print(vn)
print(type(vn))
a=6
print(bin(a))
A=9430628102
print(bin(A))
    #   Nested if else statement
a=2
b=5
c=6
d=3
if (a>b):
    print("a is greater than b ")
    if(c>d):
        print("c is greater than d")
    else:
        print("d is greater than c")
else:
    print("b is greater than a")
    #   if elif statement
a=10
b=10
if (a>b):
    print("a is greater than b") 
elif (a==b):
    print("a is equal to b") 
elif (a<b):
    print("a is smaller than b")
    #    if elif else statement
Day=("Friday")
if(Day=="Monday" or Day=="monday"):
    print("today is Monday")  
elif(Day=="Tuesday" or Day=="tuesday"):
    print("today is Tuesday")
elif(Day=="Wednesday" or Day=="wednesday"):
    print("today is Wedneday")
else:
    print("today is Holiday")
    # while loop
a=2
while(a<=20):
    print(a)
    a=a+2
    # while loop with else
a=3
while(a<=15):
    print(a)
    a=a+3
else:
    print("condition is False")
    
    #   infinite while loop
i=0
while True:
    i=i+1
    print(i)
    if(i==4):
        break

    #   Nested while loop
i=1
while i<=3:
    print("outer loop", i)
    i=i+1
    j=1
    while (j<=5):
        print("inner loop" , j)
        j=j+1
       #  Range function
a="😁😀😀"
print( "Good Morning" , a)
a=range(1,11,2)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
     # for loop
st = "Abhijeet"
for ch in st:
    print(ch)
a=range(3,10,2)
for i in a:
    print(i)
for i in range(1,5,2):
    print(i)
st="Abhishek"
n=len(st)
for i in range(n):
    print(i, "=",st[i])
