def staircase(n, pattern='#'):
    n = int(n)
    if 0 < n <= 30:
        for i in range(1, n+1):
            print(' ' * (n-i) + pattern * i)
    else:
        print('out of size')