
waiting = ['sen', 'ben', 'john']
waiting.sort() #ordenar lista por orden alfabetico
#waiting.sort(reverse=True) codigo para ordenar una lista de forma ascendente....
for index, i in enumerate(waiting):
    print(f'{index + 1}.{i.capitalize()}')
