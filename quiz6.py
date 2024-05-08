import random
ansASC = random.randint(97, 123)
ans = chr(ansASC)

def histo(g):
    a, e, i, m, q, u, u, y = 0
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
    if ord(u) >= ord('m') and ord(g) <= ord('x'):
        u += 1
    if ord(y) >= ord('m') and ord(g) <= ord('p'):
        y += 1
    print('a-d:', "*" * a,'\n','e-h:', "*" * e,'\n','i-l:', "*" * i,'\n','m-p:', "*" * m,'\n','i-l:', "*" * i,'\n','q-t:', "*" * q,'\n','i-l:', "*" * i,'\n','u-x:', "*" * u,'\n','y-z:', "*" * y,'\n')

def guess():
    n = 1
    userans = 0
    while userans == 0:
        g = input('Guess the lowercase alphabet : ')
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
            n += 1 
            break     
        if ord('g') <= 97 or ord('g') >= 122:
            print('Guess a lowercase alphabet : ')
            
    return




guess()