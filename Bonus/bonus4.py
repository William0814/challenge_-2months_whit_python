countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

for c, f in zip(countries, filenames):
    #file = 'files/zip.txt'
    file =open(f, 'w')
    file.write(c)
    file.close()
    #print(c, f)
