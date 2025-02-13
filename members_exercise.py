new_name = str(input('Enter new name: '))+'\n'
new_name = new_name.strip()
file = open('members.txt', 'r')
reads = file.readlines()
file.close()
reads.append(new_name.title())
file = open('members.txt', 'w')
file.writelines(reads)
file.close()