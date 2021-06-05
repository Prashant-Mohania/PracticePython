def matchWords(s1, s2):
    words1 = s1.split(" ")
    words2 = s2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == "__main__":
    lsts = ["Python is good", "I am good in python",
            "Python is based on OOPs (Object Oriented Programing)"]
    search = input("Search:- ")
    scores = [matchWords(search, lst) for lst in lsts]
    # print(scores)
    scores = [scores[i] for i in range(0, len(scores)) if scores[i] != 0]
    result = [r for r in sorted(zip(scores, lsts), reverse=True)]
    print(f"{len(scores)} result found")
    for i in range(0, len(result)):
        if result[i][0] != 0:
            print(i+1, "\t", result[i][1])
