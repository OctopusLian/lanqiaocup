M = int(input())
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(M):
    number = int(input())
    numbers.remove(number)
    numbers.insert(0, number)
    for n in numbers:
        print(n, end=' ')
    print('\n')
