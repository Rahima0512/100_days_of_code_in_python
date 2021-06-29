Placeholder="[name]"
with open("Input/Names/invited_names.txt",mode="r") as names:
    name_list=names.readlines()

with open("Input/letters/starting_letter.txt",mode="r") as letter:
    content=letter.read()
    for name in name_list:
        stripped_name=name.strip()
        new_letter=content.replace(Placeholder,stripped_name)
        with open(f"Output/readytosend/{stripped_name}_letter.txt",mode="w") as new_letter_generator:
            new_letter_generator.write(new_letter)





