#Create a random variable
import random
'''random_int =random.randint(1,10)
print(random_int)
random_float=random.random()*5 #this will give number in range of (0,5]
print(random_float)'''

#Random seed
'''test_seed=int(input("Create a seed number"))
random.seed(test_seed)
rand_side=random.randint(0,1)
if rand_side==1:
    print("Head")
else:
    print("Tail")
    '''
#List introduction
'''test_seed=int(input("Create a seed number"))
random.seed(test_seed)
names_as_whole=input("Enter everyone's name separated by commmas , ")
name=names_as_whole.split(", ")
print(name)
print(f"{random.choice(name)} is going to pay the bill today")'''

#Nested list introduction
'''row1=[" @ "," @ "," @ "]
row2=[" @ "," @ "," @ "]
row3=[" @ "," @ "," @ "]
map=[row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}' )
treasure=input("Where you wanna keep your treasure")
c=int(treasure[0])-1
r=int(treasure[1])-1
map[r][c]=" $ "  '''
'''if r==1 :
    row1[c]=" $ "
elif r==2 :
    row2[c]=" $ "
elif r==3:
    row3[c]=" $ "'''
'''
print("AFTER UPGRADING ::::")
print(f'{row1}\n{row2}\n{row3}' )'''
#ROCK PAPER SCISSORS
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice=int(input("Enter your choice for rock 0 paper 1 scissors 2\n"))
print("YOU ")
You=[rock,paper,scissors]
print(You[choice])
comp=random.randint(0,2)
computer=[rock,paper,scissors]
print("COMPUTER")
print(computer[comp])
if comp==choice:
    print("GAME IS DRAW")
elif choice==0 and comp==2:
    print("You win against computer!!")
elif choice==1 and comp==0:
    print("You win against computer!!")
elif choice==2 and comp==1:
    print("You win against computer!!")
elif comp==0 and choice==2:
    print("Computer wins against you !!")
elif comp==1 and choice==0:
    print("Computer wins against you!!")
elif comp==2 and choice==1:
    print("Computer wins against you!!")

