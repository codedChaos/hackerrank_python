if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        i = input().split()
        functn = i[0]
        args = tuple(i[1:])
        if functn != 'print':
            if functn == 'pop' and len(arr) == 0:
                continue
            else:
                cmd = functn + "(" + ",".join(args) + ")"
                eval("arr."+cmd)
        else:
            print(arr)
