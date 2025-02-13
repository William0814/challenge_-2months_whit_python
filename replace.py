filenames = ['1.doc', '2.report', '3.presentation']
filenames = [filename.replace('.','-')+'.txt' for filename in filenames]
print(filenames)

new = [i for i in ['a', 'b', 'c']]
print(new)