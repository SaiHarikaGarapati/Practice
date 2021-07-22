def mid_letter(string):
    if len(string) % 2 == 0:
        print("Empty String")
    else:
        n = len(string)//2
        print(n)
        print(string[n])


mid_letter("abc")




