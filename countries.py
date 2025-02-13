countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
extens = '.txt'
for c in countries:
    file_name = f'{c}{extens}'
    file = open(file_name, 'w')
    file.write(c)
    file.close()