def wrap(string, max_width):
    num, remainder = divmod(len(string), max_width)
    text = list()
    count, width = 0, max_width

    for i in range(num):
        width = (width + max_width) if count > 0 else max_width
        text.append(string[count * max_width:width])
        count += 1
        print(count, max_width, count * max_width, width, text)

    if remainder:
        text.append(string[count * max_width:width + remainder])
        print(count, remainder, text)

    return text


if __name__ == '__main__':
    #string, max_width = input(), int(input())
    result = wrap('ABCDEFGHIJKLMNOPQRSTUVWXY', 4)
    print(*result, sep='\n')
