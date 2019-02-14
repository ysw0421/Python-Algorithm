'''
평균 점수
숏코딩:
print(eval("+max(8,int(input())//5)"*5))
'''
sum = 0
for i in range(0,5):
    value = int(input())
    if value <= 40 :
        value = 40
    sum += value
print(int(sum/5))
