s = {'name': "Prashant", 'grade': [80, 50, 79, 55]}

def avg(std):
    return sum(s['grade'])/ len(s['grade'])
# res = avg(s)
# print(res)
# print("file", __name__)

if __name__ == "__main__":
    res = avg(s)
    print(res)
    print("file", __name__)