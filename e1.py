import glob

file = glob.glob('files/*.txt')
for i in file:
    with open(i,'r') as file:
        print(file.read().title())


