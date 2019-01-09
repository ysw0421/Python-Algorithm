'''
셀프 넘버
숏코드 : r=range(9999);print(*sorted({*r}-{n+sum(map(int,str(n)))for n in r}))
'''
def SelfNum(val):
    digits = len(str(val))
    sum = 0
    for i in range(digits):
        sum += int(val%(10**(i+1))/(10**i))
    return val + sum

result = set(range(1,10001))
Unnecessary = set()
for i in range(1, 10001):
    Unnecessary.add(SelfNum(i))

result=result-Unnecessary

for i in sorted(result):
    print(i)
