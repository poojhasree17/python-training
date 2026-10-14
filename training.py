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
elif num_1%3==0:
    print("only divisble by 3")
elif num_1%5==0:
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
elif num_1%3==0:
    print("only divisble by 3")
elif num_1%5==0:
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

#count the number divisble by 5
count=0
for d in range (1,51):
    if d%5==0:
        count+=1
        print(d)
print("count",count)

#sum of odd numbers
sum=0
for i in range(1,21):
    if i%2!=0:
        sum+=i
print("sum of odd numbers:",sum)

#print the numbers which are divisble by 3 but not by 2
for i in range(1,31):
    if i%3==0 and i%2!=0:
        print(i)
    else:
        pass

#count the positive and negative numbers
count_pos=0
count_neg=0
num=[-1,2,-3,4,-5,6,-7,8,-9,10]
#num=input("enter the numbers separated by space:").split()
for i in num:
    #i=int(i)
    if i>0:
        count_pos+=1
    elif i<0:
        count_neg+=1
print("count of positive numbers:",count_pos)   
print("count of negative numbers:",count_neg)

#factorial of a number
num=int(input())
factorial=1
for i in range(1,num+1):
    factorial*=i
print(factorial)

#prime number or not
num=int(input())
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
    else:
            print("prime")
else:
     print("invalid input")

#find the largest number in a list
# num=[5,88,8,76,9,45,23,67,12]
num=input("enter the numbers separated by space:").split()
largest=int(num[0])
for i in num:
    i=int(i)
    if i>largest:
        largest=i
print(largest)

#armstrong number or not
num=int(input("enter the number:"))
num_str=str(num)
num_len=len(num_str)
sum=0
for i in num_str:
    sum+=int(i)**num_len
if sum==num:
        print("armstrong number")
else:
        print("not armstrong number")

#sum of four digit number
num=int(input())
sum=0
while num>0:
       digit=num%10
       sum+=digit
       num=num//10
print(sum)

#1.automorphic or not
def automorphic(num):
    return (num*num)%(10**len(str(num)))==num
print(automorphic(11))

#2.automorphic or not
num=int(input())
n=num*num
if str(n).endswith(str(num)):
    print("auto")
else:
    print("not auto")

#neon number or not
num=int(input())
sq=num*num
sum=0
for i in str(sq):
    sum+=int(i)
if sum==num:
    print("neon")
else:
     print("not neon")

#palindrome or not
num=int(input())
if str(num)==str(num)[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#perfect number or not
num=int(input())
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("perfect!")
else:
    print("not perfect!")
