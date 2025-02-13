from functions import get_employs
file = open('files/dates.txt', 'r')
content = file.read()
file.close()
total = len(content)
print('The file contains ', f'{total}', 'characters')
