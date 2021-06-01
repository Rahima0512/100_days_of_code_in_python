#find Even and odd
"""
n=int(input("Enter the number you wanna check \n"))
if (n%2==0) :
    print("that's an even number")
else :
    print("that's an odd number")
"""
#Nested else if
"""
print("Welcome to the rollar coaster ride")
height=int(input("Enter your height in cm"))
if height>=120:
    print("You are allowed")
    age=int(input("Enter your age\n"))
    if age<18:
        print("pay 250")
    elif age>=18 and age<45:
        print("pay 170")
    elif age>=45 and age<=55:
        print("Tadaaaaaaaaa!!!! Free ticket")

else :
    print("You are not allowed")

"""

#Leap year
"""
year=int(input("Enter the year"))
if year%4==0 :
    
        if (year%100 !=0) : 
            print(f"{year} is a leap year")
            
        else :
            if (year%400==0):
                print(f"{year} is a leap year")
            else :
                    print(f"{year} is a not leap year")
            
            
else :
     print(f"{year} is a not leap year")
    
"""
#Pizza order challlenge
"""price=0
print("Welcome to the pizza hut")
size=input("Enter the size L M R\n")
pepperoni=input("Want to add pepperoni? Y/N\n")
extra_cheese=input("Want to add extra cheese? Y/N\n")
if size=="L":
    price=25
    if pepperoni=='Y':
        price+=2
if size=='M':
    price=20
    if pepperoni=='Y':
        price+=3
if size=='R':
    price=15
    if pepperoni=='Y':
        price+=3

if extra_cheese=='Y':
    price+=1

print(f"Your final bill is {price}")

"""
#LOVE CalculATOR
print("Welcome to the love calculator")
name_1=input("Your name please\n")
name_2=input("Your crush's name please\n")

name_1=name_1.lower()
name_2=name_2.lower()

T=(name_1.count("t"))+(name_2.count("t"))
R=name_1.count("r")+name_2.count("r")
U=name_1.count("u")+name_2.count("u")
E=name_1.count("e")+name_2.count("e")

L=(name_1.count("l"))+(name_2.count("l"))
O=name_1.count("o")+name_2.count("o")
V=name_1.count("v")+name_2.count("v")
E=name_1.count("e")+name_2.count("e")
digi_1=T+R+U+E
if digi_1<10 and digi_1>0:
    digi_1+=10

digi_2=L+O+V+E
percnt=digi_1+digi_2
print(f"Your love percentage is {percnt}%")
if percnt<10 or percnt>90:
    print("Your are like coke and mentos!")
elif percnt>40 and percnt<50:
    print("You are alright together!")