with open("./Input/Letters/starting_letter.txt") as letter:
    template = letter.read()

with open("./Input/Names/invited_names.txt") as name_list:
    names = name_list.readlines()

for name in names:
    new_name = name.strip()
    new_letter = template.replace("[name]", new_name)
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)
