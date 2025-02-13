waiting_list = ["john", "marry", "william"]
print('Names exiting: "john", "marry", "william"')
name = input("Enter name: ")
try:
    number = waiting_list.index(name)+1
    print(f"{name}'s turn is {number}")

except ValueError:
    print(f"{name} is not in the list.")