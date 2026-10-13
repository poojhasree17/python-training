<<<<<<< HEAD
#odd or even
num=int(input())
result="even" if (num%2==0) else "odd"
print(result)

#positive or negative
n=int(input())
r= "positive" if (n>=0) else "negative"
print(r)

#largest of 2 numbers
v=int(input())
w=int(input()) 
if v>w:
    print(v,"is largest")
else:
    print(w,"is largest")  

#voting eligiblity
age=int(input())
if age>=18:
    print("eligible")
else:
    print("not eligible")

#pass or fail
mark=int(input())
if mark>=45:
    print("pass")
else:
    print("fail")

#greatest of three numbers
#if,elif,else
x=45
y=23
z=34
if x>y and x>z:
    print("x is greater")
elif y>x and y>z:
    print("y is greater") 
else:
    print("z is greater")

#leap year
#divisble by 4 and not divisble by 100 or divisble by 400 says leap year
year=int(input("enter the year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("it  is a leap year")
else:
    print("it is not a leap year")

#CALCULATOR PROGRAM TO PERFROM OPERATIONS INSIDE A FUNCTION AND TO CONTINUE THE CALCULATIONS BY WHILE LOOP
def Calculator(a,b):#defining the function with two parameters
     def Add():
         return a+b
     def Sub():
         return a-b
     def Mul():
         return a*b
     def Div():
         return a/b
     
     print("addition:",Add())
     print("subtraction:",Sub())
     print("multiplication:",Mul())
     print("division:",Div())
while True:#to create the loop to continue until the user wants to stop     
 Calculator(5,3)#calling the function 
 choice=input("do you want to continue?")
 if choice=="n":
     break
 else:
    continue

#divisble by 3 or 5
num_1=int(input())
if num_1%3==0 and num_1%5==0:
    print("divisble by 3 and 5")
elif num%3==3:
    print("only divisble by 3")
elif num%5==0:
    print("only divisble by 5")
else:
    print("not divisble by both")

#eligble for discount or not
cust_age=int(input())
if cust_age<=18:
    print("eligible")
else:
    print("not eligible")

#two digit or not
digit=int(input())
if digit>=10 and digit<100:
    print("it is a two two digit")
else:
    print("not")
=======
#odd or even
num=int(input())
result="even" if (num%2==0) else "odd"
print(result)

#positive or negative
n=int(input())
r= "positive" if (n>=0) else "negative"
print(r)

#largest of 2 numbers
v=int(input())
w=int(input()) 
if v>w:
    print(v,"is largest")
else:
    print(w,"is largest")  

#voting eligiblity
age=int(input())
if age>=18:
    print("eligible")
else:
    print("not eligible")

#pass or fail
mark=int(input())
if mark>=45:
    print("pass")
else:
    print("fail")

#greatest of three numbers
#if,elif,else
x=45
y=23
z=34
if x>y and x>z:
    print("x is greater")
elif y>x and y>z:
    print("y is greater") 
else:
    print("z is greater")

#leap year
#divisble by 4 and not divisble by 100 or divisble by 400 says leap year
year=int(input("enter the year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("it  is a leap year")
else:
    print("it is not a leap year")

#CALCULATOR PROGRAM TO PERFROM OPERATIONS INSIDE A FUNCTION AND TO CONTINUE THE CALCULATIONS BY WHILE LOOP
def Calculator(a,b):#defining the function with two parameters
     def Add():
         return a+b
     def Sub():
         return a-b
     def Mul():
         return a*b
     def Div():
         return a/b
     
     print("addition:",Add())
     print("subtraction:",Sub())
     print("multiplication:",Mul())
     print("division:",Div())
while True:#to create the loop to continue until the user wants to stop     
 Calculator(5,3)#calling the function 
 choice=input("do you want to continue?")
 if choice=="n":
     break
 else:
    continue

#divisble by 3 or 5
num_1=int(input())
if num_1%3==0 and num_1%5==0:
    print("divisble by 3 and 5")
elif num%3==3:
    print("only divisble by 3")
elif num%5==0:
    print("only divisble by 5")
else:
    print("not divisble by both")

#eligble for discount or not
cust_age=int(input())
if cust_age<=18:
    print("eligible")
else:
    print("not eligible")

#two digit or not
digit=int(input())
if digit>=10 and digit<100:
    print("it is a two two digit")
else:
    print("not")

#find the last digit
x=int(input())
print("last digit:", x%10)

#sum of first digit and last digit
digit=int(input())
last=digit%10
while digit>=10:
    digit=digit//10
first=digit
print(first,last)
print(first+last)

#swapping of two number without temp var
a=10
b=20
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)

#find the range of the number
range=int(input())
if (range>=20 and range<=60):
    print("lies in range")
else:
    print("not lies in range")

#find the triangle is valid or not
x=int(input())
y=int(input())
z=int(input())
if x>=0 and y>=0 and z>=0:
    if((x+y>z and y+z>x and z+x>y)):
        print("valid triangle")
    else:
        print("not a valid triangle")
else:
    print("invalid input")
>>>>>>> 8adac92 (python)
