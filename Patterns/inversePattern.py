n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=n-i:
        print(' ',end = '')
        j+=1
    stars = 1
    while stars <= i:
        print('*',end = '')
        stars+=1
    print()
    i+=1