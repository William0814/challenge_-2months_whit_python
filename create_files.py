languages = ['English', 'German', 'Spanish']

for i in languages:
    #new_file = f"{i}.txt"
    with open(f"{i}.txt", "w") as file:
        file.write(i)
        