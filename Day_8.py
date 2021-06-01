import math
def greet(name,location):
    {
        print(f"Hiiiii babes! {name} I know you live in {location}")

    }

greet("Rahima","Patna")
greet(location="Kanpur",name="Afshan")

'''def no_of_can(height,width,cover):
    
    requirement=math.ceil((height*width)/cover)
    print(f"Cans required are {requirement}")

height=int(input("Enter height \t"))
width=int(input("Enter width \t"))
cover=int(input("Enter cover \t"))
no_of_can(height,width,cover)'''

'''def prime_checker(number):
    m=math.ceil(number/2)
    count=True
   
    for i in range (2,m):
        
        if(number%i==0):
            count=False
            break    
        
    if(count==True):
        print("It is a prime number")
    if(count==False):
        print("It is not a prime number")
n=int(input("Enter the number "))
number=n
prime_checker(number)'''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

text=input("Enter your text").lower()
shift=int(input("Enter the shift amount"))
def split(word):
  list1=[]
  list1[:0]=word
  return list1
text=split(text)


def encoder(text,shift):
    cipher_text=""
    for x in text:
        position=letters.index(x)
        new_position=position+shift
        cipher_text+=letters[new_position]
    print(f"Your encoded text is {cipher_text}")

encoder(text,shift)                 
                   
        