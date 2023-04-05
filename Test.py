N = int(input("Введите кол-во строчек:"))
lst = [list(map(int, input().split())) for i in range(N)]
print(*lst)
