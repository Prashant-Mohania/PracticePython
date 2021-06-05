def common(n1 , n2):
    output = []
    for i in n1:
        if i in n2:
            output.append(i)
    return output
a = [1,4,5,8]
b = [2,4,8,6]
print(common(a,b))