#! python3
"""Scratch Pad 2 for Python

Place for hacking python together and testing.
"""


def callFuncs(o, f):
    try:
        r = getattr(o, str(f))()
    except ValueError as e:
        return e
    return r


def getStrCharTypes(string):
    tests = {'isalnum': False,
             'isalpha': False,
             'isdigit': False,
             'islower': False,
             'isupper': False}
    for char in string:
        for func in list(tests.keys()):
            try:
                result = callFuncs(char, func)
            except ValueError as e:
                return(e)
            if tests[func] != True:
                tests[func] = result
    return tuple(tests.values())


if __name__ == '__main__':
    s = input()
    try:
        result = getStrCharTypes(s)
    except ValueError as e:
        print(e)
        quit()
    for res in result:
        print(res)
