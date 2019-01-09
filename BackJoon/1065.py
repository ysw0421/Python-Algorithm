'''
정수 X의 자리수가 등차수열, 한수
숏코딩 : print(sum(i//100+i%10==i//10%10*2 or i<100 for i in range(1,int(input())+1)))
'''
def Series(Num):
    if Num < 100:
        return int(1)
    else:
        List = []
        for i in str(Num):
            List.append(i)
        if 2*int(List[1]) == int(List[0]) + int(List[2]):
            return int(1)
        else:
            return int(0)
n = int(input())
result = 0
for j in range(1,n+1):
    result += Series(j)
print(result)
