##  @package runnerup_in_list
#   Documentation for this program
#
#   More Details.

from more_itertools import locate


def findAllIndexesOfValue(arr_list, w):
    ##  Documentation for Lambda function
    #   using the locate function from more_itertools library
    #   find all indexes of the given number with a lambda
    #   comparison
    wl = list(locate(arr_list, lambda a: a == w))
    return wl


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner = max(arr)
    print("winner: ", winner)

    winners_list = list(findAllIndexesOfValue(arr, winner))

    print("winners_list : ", winners_list)
    for r in range(len(winners_list)):
        print("r: ", r)
        try:
            arr.pop(arr.index(winner))
        except ValueError as e:
            print(e)
            continue

    print("new array: ", arr)
    runnerup = max(arr)
    print("runnerup : ", runnerup)
