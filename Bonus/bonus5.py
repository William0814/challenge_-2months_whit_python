password = input('Enter new password: ')
result = {}

if len(password) >= 8:
    result ["lenght"] = True
else:
    result ["lenght"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result ["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result ["upper-case"] = uppercase
print(result)

if all(result.values()):
    print('Password is strong and correct')


else:
    print('Password is not secure...')