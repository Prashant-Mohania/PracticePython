p1, p2, p3, p4, p5 = input("Enter :- ").split(" ")

print("Error" if p1 < (p2+p3+p4+p5) and p2 < (p1+p3+p4+p5) and p3 < (p1+p2+p4+p5) and p3 < (p2+p1+p4+p5) and p4 < (p2+p3+p1+p5) and p5 < (p2+p3+p4+p1) else "Ok")
