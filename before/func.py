def greater(a,b):
        if a > b:
                return a
        else:
                return b

def new_g(a,b,c):
        # bigger = greater(a,b)
        return greater(greater(a,b),c)
x=int(input("enter:- "))
y=int(input("enter:- "))
z=int(input("enter:- "))
new_g(x,y,z)

print(new_g(x,y,z))