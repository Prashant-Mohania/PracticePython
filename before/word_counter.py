def wordcounter(n):
    count = {}
    for i in n:
        count[i] = n.count(i)
    return count


print(wordcounter("Prashant"))


def wordcounter(n):
    count = {}
    for i in n:
        count[i] = n.count(i)
    for key, value in count.items():
        print(f"{key} = {value}")


wordcounter("Prashant")
