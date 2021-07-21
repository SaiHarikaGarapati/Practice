def capital_indices(str1):
    l = list(str1)
    print(l)
    indeces = []
    for i in range(0,len(l)):
        if l[i].isupper():
            indeces.append(i)
    print(list(indeces))

capital_indices("HeLlO")