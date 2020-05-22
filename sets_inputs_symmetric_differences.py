#! python3

# grab 4 inputs from stdin, select only the 4th and 2nd inputs (lists being provided, while 1st
# and 3rd are lengths of the lists). Then sort and pull the symmetric differences using the ^
# operator between the two sets "a^b". and separate those outputs using '\n' before printing.

if __name__ == '__main__':
    a,b = [set(input().split()) for _ in range(4)][1::2]
    print(*sorted(a^b, key=int), sep='\n')