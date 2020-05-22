#! python3
"""Scratch Pad 2 for Python

Place for hacking python together and testing.
"""


def delScore(list1, num):
    """
    Delete score from passed list.

    Accepts 2 arguments of types (list, num). Remove 'num' from 'list' with del().
    Returns modified list().
    """
    try:
        list1 = [x for x in list1 if x[1] != num]
    except:
        return(ValueError)
    return list1


def iterNestedList(list1, index):
    for i in list1[index]:
        if type(i) in (complex, float, index):
            return type(i)(i)
        else:
            continue


def findLowScore(lst1):
    """
    Find the lowest score in passed list.

    Accepts a list() as an argument. Searches through list to find the lowest score.
    Returns low_score number.
    """
    l_score = None
    print("findLowScore: entry")
    try:
        l_score = iterNestedList(lst1, 0)
    except ValueError as e:
        print("valueError: ", e)

    try:
        for score in lst1:
            if score[1] < l_score:
                l_score = score[1]
    except ValueError as e:
        return(e)
    print("l_score: ", l_score)
    return l_score


if __name__ == '__main__':
    sg_orig = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        sg_orig.append([str(name), float(score)])

    low_score = findLowScore(sg_orig)
    sg_new = delScore(sg_orig, low_score)
    low_score = findLowScore(sg_new)
    fin_list = [sg_new[x]
                for x in range(len(sg_new)) if sg_new[x][1] == low_score]
    fin_list.sort()

    for x in fin_list:
        print(x[0])
