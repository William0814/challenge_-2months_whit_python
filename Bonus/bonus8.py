from converts import convert
from parses import parse

feet_inches = input("Enter your height in feet and inches, separated by a space: ")

feet, inches = parse(feet_inches)

result = convert(feet, inches)
print(result)

