import random
from turtledemo.penrose import start

user_number1 = int(input('Enter first number: '))
user_number2 = int(input('Enter second number: '))

number_random = random.randint(user_number1, user_number2)

print(number_random)

