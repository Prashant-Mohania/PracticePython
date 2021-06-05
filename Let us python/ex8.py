# -----------------------   A - a   -------------------------


# tpl1 = (8, 3, 2021)
# tpl2 = (22, 4, 2022)

# days = 0


# if tpl1[2] == tpl2[2]:
#     if tpl1[1] == tpl2[1]:
#         if not tpl1[0] == tpl2[0]:
#             days += abs(tpl1[0]-tpl2[0])
#         else:
#             print("Dates are same")
#     else:
#         for m in range(abs(tpl1[1]-tpl2[1])):
#             days += 30
#         if not tpl1[0] == tpl2[0]:
#             days += abs(tpl1[0]-tpl2[0])
#         else:
#             print("Dates are same")
# else:
#     for y in range(abs(tpl1[2] - tpl2[2])):
#         days += 365
#     if tpl1[1] == tpl2[1]:
#         if not tpl1[0] == tpl2[0]:
#             days += abs(tpl1[0]-tpl2[0])
#         else:
#             print("Dates are same")
#     else:
#         for m in range(abs(tpl1[1]-tpl2[1])):
#             days += 30
#         if not tpl1[0] == tpl2[0]:
#             days += abs(tpl1[0]-tpl2[0])
#         else:
#             print("Dates are same")

# print(days)


# -----------------------   A - b   -------------------------


# tplLst = [("Mobile", 10999.00), ("EarPhone", 999.00)]

# print(sorted(tplLst))


# -----------------------   A - c   -------------------------


# userShare = ("Prashant Mohania", 8-3-21, 50, 5, 1000)

# tcp = userShare[2]*userShare[3]
# tsp = userShare[4]*userShare[3]
 
# print("Total cost of porfolio :- ", tcp)
# print("Total amout gain or lost :-", tsp - tcp)
# print("Percentage  profit made or loss incurred :-", (tsp - tcp)*tcp/100)


# -----------------------   A - d   -------------------------


tplLst2 = [(1,), (), (1, 5, 3), ()]

for i in tplLst2:
    if len(i) == 0:
        tplLst2.remove(())
print(tplLst2)