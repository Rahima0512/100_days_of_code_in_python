import pandas
data=pandas.read_csv("Squirrel_Data.csv")

grey_squirrel_count=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrel_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel_count=len(data[data["Primary Fur Color"]=="Black"])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)
data_dict={
    "Colour":["Grey","Cinnamon","Black"],
    "Count":[grey_squirrel_count,red_squirrel_count,black_squirrel_count]
}

new_book=pandas.DataFrame(data_dict)
new_book.to_csv("50_states.csv")
