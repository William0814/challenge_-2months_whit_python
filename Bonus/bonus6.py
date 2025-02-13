try:
    width = float(input('Enter rectangle width: '))
    length = float(input('Enter rectangle length: '))
    if width == length:
        exit('Same values, is not correct.')
except ValueError:
    print('Please enter a number.')