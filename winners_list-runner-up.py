#! python3
# scratch 2


def getIndexPositions(listOfElements, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    indexPosList = []
    indexPos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            indexPos = listOfElements.index(element, indexPos)
            # Add the index position in list
            indexPosList.append(indexPos)
            indexPos += 1
        except ValueError as e:
            print(e)
            break
    return indexPosList


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner = max(arr)
    winners_list = list(getIndexPositions(arr, winner))
    print("winners_list (indexes of winning score(s)): ", winners_list)
    for i in range(len(winners_list)):
        try:
            arr.pop(arr.index(winner))
        except ValueError as e:
            print(e)
            continue

    runner_up = max(arr)
    print("runner-up : ", runner_up)
