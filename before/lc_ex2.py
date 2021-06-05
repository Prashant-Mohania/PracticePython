def num(n):
    return [str(i) for i in n if (type(i) ==  int or type(i) == float) ]
print(num([True , False , [1,2,3] , 1 , 2 , 1.0 , 3]))

seperate = {i : 'even' if i%2==0 else 'odd' for i in range(1,11)}
print(seperate)