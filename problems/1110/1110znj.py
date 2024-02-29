ls = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
m = int(input())
shuru = [str(input()) for i in range(m)]
for i in shuru:
    ls.remove(i)
    ls.insert(0, i)
    print(' '.join(ls))
