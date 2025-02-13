with open("Belgium") as file:
    new_file = file.read()
    with open("copy_belgium.txt", "w") as file1:
        file1.write(new_file)
