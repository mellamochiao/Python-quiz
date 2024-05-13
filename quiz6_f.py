import random
ansASC = random.randint(97, 123)
ans = chr(ansASC)

def histo(g):
    global a, e, i, m, q, u, y
    if ord(g) >= ord('a') and ord(g) <= ord('d'):
        a += 1
    if ord(g) >= ord('e') and ord(g) <= ord('h'):
        e += 1
    if ord(g) >= ord('i') and ord(g) <= ord('l'):
        i += 1
    if ord(g) >= ord('m') and ord(g) <= ord('p'):
        m += 1
    if ord(g) >= ord('q') and ord(g) <= ord('t'):
        q += 1
    if ord(g) >= ord('u') and ord(g) <= ord('x'):
        u += 1
    if ord(g) >= ord('y') and ord(g) <= ord('z'):
        y += 1
    return a, e, i, m, q, u, y

def guess():
    n = 1
    global a, e, i, m, q, u, y
    userans = 0
    while userans == 0:
        g = input('Guess the lowercase alphabet : ')
        histo(g)
        while ord(g) >= 97 and ord(g) <= 122:
            if ord(g) > ansASC:
                n += 1    
                print('The alphabet you are looking for is alphabetically lower')
                break
            if ord(g) < ansASC:
                n += 1 
                print('The alphabet you are looking for is alphabetically higher')
                break
            else:
                userans = 1
                print('Congrats! You Guess the alphabet',ans,'in',n,'tries.')
                print('a-d:', "*" * a,'\n''e-h:', "*" * e,'\n''i-l:', "*" * i,'\n''m-p:', "*" * m,'\n''q-t:', "*" * q,'\n''u-x:', "*" * u,'\n''y-z:', "*" * y,'\n')
                print(a, e, i, m, q, u, y)
            n += 1 
            break     
        if ord('g') <= 97 or ord('g') >= 122:
            print('Guess a lowercase alphabet : ')
    return

a, e, i, m, q, u, y = 0, 0, 0, 0, 0, 0, 0
guess()