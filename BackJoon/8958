'''
OX 퀴즈
숏코딩:
exec("print(sum([n*-~n//2for n in map(len,input().split('X'))]));"*int(input()))
'''
count = int(input())
case = []
for i in range (0,count):
    case.append(input())
for i in range (0,len(case)):
    sum = 0
    for j in range(0, len(case[i].split("X"))):
        n = case[i].split("X")[j].count("O")
        sum += int(n * (n + 1) / 2)
    print(sum)
