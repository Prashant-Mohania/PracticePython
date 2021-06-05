# first method:- by pop and append


def reverse_list(n):
    mun = []
    for i in range(len(n)):
        popped = n.pop()
        mun.append(popped)
    return mun


num = [1, 2, 3, 4]
print(reverse_list(num))


# second mothod:- by reverse method


def rev(n):
    n.reverse()
    return n


num = [1, 2, 3, 4]
print(rev(num))


# third method:- by slicing

def ulta(n):
    return n[::-1]


num = [1, 2, 3, 4]
print(ulta(num))
