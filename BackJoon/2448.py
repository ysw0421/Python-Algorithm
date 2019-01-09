'''
3*2^k 별 찍기
숏코딩:
N=int(input())
r=['*','* *','*'*5]
i=6
while i<=N:r+=[s.ljust(i)+s for s in r];i*=2
for s in r:print(s.center(i-1))
'''
import math
star = ['  *   ', ' * *  ', '***** ']
def StarsTower(Move):
    for i in range(len(star)):
        star.append(star[i] + star[i])
        star[i] = ' ' * Move + star[i] + ' ' * Move
Num = int(input())
k = int(math.log(Num / 3, 2))
for i in range(k):
    StarsTower(2 ** i * 3)
for i in range(len(star)):
    print(star[i])
