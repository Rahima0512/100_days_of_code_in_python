letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
ans='y'


def caesar(direction,text,shift):
    cipher_text=""
    for x in text:
        position=letters.index(x)
        if direction=='decode':
            shift*=-1
        new_position=position+shift
        cipher_text+=letters[new_position]
    print(f"Your {direction}d text is {cipher_text}")
    
    


while(ans=='y'):
    direction=input("Enter 'encode' or 'decode' text\t").lower()
    text=input("Enter your text\t").lower()
    shift=int(input("Enter the shift amount\t"))
    caesar(direction,text,shift)
    ans=input("Do you want to continue 'y'/ 'n' " )


    



    

    