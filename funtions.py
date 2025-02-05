def get_employs():
    with open('Employs.txt', 'r') as file:
        employs = file.readlines()
    return employs