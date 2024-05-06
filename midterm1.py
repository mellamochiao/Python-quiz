n = 9   # all start from 9
while n >= 3:
    i = 9
    while i >= 1:
        x = 0
        while x <= 2:
            print(i, 'x', n-x, '=', i*(n-x), '\t', end = '')
            x += 1
        print('')
        i -= 1
    print('')
    n -= 3