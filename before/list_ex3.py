def ulta(n):
    word = []
    for i in n:
        word.append(i[::-1])
    return word
elements = ["abc" , "pqr" , "xyz"]
print(ulta(elements))