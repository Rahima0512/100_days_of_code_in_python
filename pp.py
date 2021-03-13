'''1. Write a Python program to find whether a given number (accept from the user) is even or odd.'''
n=int(input("Enter the number you wanna check even/odd \n"))
if (n%2==0) :
    print("that's an even number")
else :
    print("that's an odd number")

'''2.Any year is input through the keyboard. Write a program to determine whether the year is a leap year or not.
'''
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

'''3.Program to find the smallest number among three numbers.'''
num1=int(input("Enter the number you wanna check \n"))
num2=int(input("Enter the number you wanna check \n"))
num3=int(input("Enter the number you wanna check \n"))

if(num1<num2) and (num1<num3):
    print(f"Smallest number is {num1}")
elif(num2<num1) and (num2<num3):
    print(f"Smallest number is {num2}")
else:
    print(f"Smallest number is {num3}")

'''
    
4. Any year is input through the keyboard. Write a program to determine whether the year is a leap year or not using logical operators'''

year1=int(input("Enter the year"))
if year1%400==0 and (year1%100 !=0) :
    print(f"{year1} is a leap year")
else:
    print(f"{year1} is a not leap year")

'''5.Python Program for Program to find area of a circle'''
r=float(input("Enter the radius"))
area=3.14*r*r
print(f"The area of the circle is {area} ")

'''6. Python program to print all Prime numbers in an Interval '''


lower = int(input("Enter the range starting"))
upper = int(input("Enter the range end"))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
  
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

'''7. Python program to check whether a number is Prime or not'''
num = int(input("Enter the number"))
if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               print(f"{num} is not a prime number") break
            

       else:
           print(f"{num} is a prime number")

'''8. Python Program for n-th Fibonacci number '''
nterms = int(input("Enter the range for series"))
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

'''9. Python Program for Sum of squares of first n natural numbers 
10. Python Program for cube sum of first n natural numbers.
'''

num=int(input("Enter the number"))
sum_of_squares=0
sum_of_cubes=0

for x in range (0,num+1):
    
        sum_of_squares+=x*x
        sum_of_cubes+=x*x*x
 
print(f"The Sum of squares of first {num} natural numbers is {sum_of_squares} and \ncube sum of first {num} natural numbers is {sum_of_cubes} ")


