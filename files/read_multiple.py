files = ['a.txt', 'b.txt', 'c.txt']
for f in files:
    file = open(f, 'r')
    content = file.read()
    print(content.title())