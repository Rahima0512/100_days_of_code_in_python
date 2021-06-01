'''student_marks={"Harry":81, "Ron":78, "hermione":99,"Draco":74,"Neville":62,}
print(student_marks)
student_grades={}
for name in student_marks:
    g=""
    if student_marks[name]>=91 and student_marks[name]<=100:
        g="Outstanding"
    if student_marks[name]>=81 and student_marks[name]<=90:
        g="Exceeds Expectation"
    if student_marks[name]>=71 and student_marks[name]<=80:
        g="Acceptable"
    if student_marks[name]<=70:
        g="Fail"
    student_grades[name]=g
print(student_grades)'''
'''

travel_log=[
    {
        "state":"Uttar_Pradesh",
        "cities_visited":["Kanpur","Lucknow","Agra"],
        "total_visit":12
        },
    {
        "state":"Bihar",
        "cities_visited":["Patna","Sasaram","Gaya"],
        "total_visit":19

    }
]

def add_new_country(country,visit,cities):
    new_book={"country":country,"cities_visited":cities,"total_visit":visit}
    travel_log.append(new_book)

add_new_country("Russia",2,["Moscow","Saint Petersbu"])
print(travel_log)'''

def clear():
    if name=='nt':
        _=system('clear')

print("***********Welcome to the auction program***********")
go_on="yes"
Bidders={}
x=[]
def import_bidder(name,bid):
    Bidders[name]=bid

while(go_on=="yes"):
    
    name=str(input("Enter your name\t"))
    bid=int(input("Enter the amount\t"))
    import_bidder(name,bid)
    go_on=input("Are there any more bidders?\t")
    for bidders in Bidders:
        x.append(bidders)
        winner=max(x)
print(x)
print(f"The winner is {winner} with a bid of {Bidders[winner]}")



