#Loop 
#avg height of a person 
'''student_height=input("Enter the height of the people ").split(", ")
total_height=0
for x in range (0,len((student_height))):
    student_height[x]=int(student_height[x])
for height in student_height :
    total_height +=height
#here sum() could be used total_height=sum(student_height)
total_student=0
for student in student_height:
    total_student +=1

print(f"Total number of student's height provided= {total_student}")
print(f"Total number of  height provided= {total_height}")
print(f"Average height= {total_height/total_student}")'''

'''student_score=input("Enter the score of the people ").split()
temp=0
for x in range (0,len((student_score))):
    student_score[x]=int(student_score[x])

#max() could be used maximum_score=max(student_score)

for score in student_score:
    
    if(score>temp):
        temp=score
    
print(f"Highest score obtained is {temp}")'''
sum1=0
#Loop using range
'''for x in range (2,101):
    if(x%2==0):sum1 +=x
print(f"Sum obtained is {sum1}")
#or 
sum1=0
for x in range (2,101,2):
    sum1 +=x
print(f"Sum obtained is {sum1}")'''
#fizz buzz game

'''for x in range (1,50):
    if(x%15==0):
        print("fizzbuzz")
    elif(x%3==0):
        print("fizz")
    elif(x%5==0):
        print("buzz")
    else:
        print(x)

'''
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list=[]
for x in range (0,nr_letters):
    password_list.append(random.choice(letters))

for x in range (0,nr_symbols):
    password_list.append(random.choice(symbols))

for x in range (0,nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
str1=""
for char in password_list :
    str1+=char


print(f"Your password is {str1}")
