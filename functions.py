def get_employs(filepath='Employs.txt'):
    """ Read a text file and return the list of Employs items."""
    with open(filepath, 'r') as file:
        employs = file.readlines()
    return employs


def write_employs(employs_arg, filepath='Employs.txt'):
    """ Write the Employ items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(employs_arg)


if __name__== "__main__":
    print("hello")