user = list(input("Enter a list:- "))
# inbuilt method
m1 = user[:]
m1.reverse()
print(m1)

# [::-1] method
m2 = user[::-1]
print(m1)

# swap first with last
m3 = user[:]
for i in range(len(m3)//2):
    m3[i], m3[len(m3) - i - 1] = m3[len(m3) - i - 1], m3[i]
print(m3)
