# method 1

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
def average_finder(*arg):
    average = []
    for i in zip(*arg):
        average.append(sum(i)/len(i))
    return average 
print(average_finder(a,b,c))

# method 2

z =lambda *arg : [sum(i)/len(i) for i in zip(*arg)]
print(z(a,b,c))
