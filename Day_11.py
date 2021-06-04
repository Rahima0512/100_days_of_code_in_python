import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user=[]
computer=[]
print("**************************************Game starts**************************************")
start=input("Do You wanna start game y/n?\t")
def hit():
    if 11 in user and sum_user > 21:
        cards.remove(11)
        cards.append(1)
    card_got = random.choice(cards)
    user.append(card_got)
def hit_comp():
    if 11 in computer and sum_computer > 21:
        cards.remove(11)
        cards.append(1)

    card_got = random.choice(cards)
    computer.append(card_got)

def is_lost():
    sum_user=sum(user)
    sum_computer=sum(computer)
    if sum_user>21:
        print(f"Computer wins with your cards {user} and computer has {computer}")
        exit()
def is_blackjack():
    if sum_user == 21 and len(user) == 2:
        print("You Win You have a blackjack")
        blackjack = True

    if sum_user == 21 and len(computer) == 2:
        print("Coputer has a blackjack!!!!!\n You Lose")
        blackjack = True


def stand():
    if(is_lost()==True):
        print("You lost")
    sum_user = sum(user)
    sum_computer = sum(computer)
    if sum_user==21 or sum_user<sum_computer:
        print(f"You WIN with a cards {user} and computer has {computer}")
        exit()
    if sum_computer==21 or sum_computer>17 and sum_computer or (sum_user<17 and sum_computer==17):
        print(f"Computer wins with your cards {user} and computer has {computer}")
        exit()
    if sum_user==sum_computer:
        print(f"*****Draw match***** your score was  {user}")
        exit()
    if sum_computer<17:
        hit_comp()
        print(computer)
        stand()

def action():
    command = input("What do you wanna do hit/stand:\t")
    if command == 'hit':
        hit()
        is_lost()
    if command == 'stand':
        is_lost()
        stand()



while(start=='y'):
    for x in range (0,2):
        card_got=random.choice(cards)
        user.append(card_got)

    print(user)
    for x in range (0,2):
        card_got=random.choice(cards)
        computer.append(card_got)
    print(f"Computer card: {computer[0]}")
    action()
    sum_user=sum(user)
    if sum_user<17:
        action()

    if (is_blackjack()==True):

        start='n'

