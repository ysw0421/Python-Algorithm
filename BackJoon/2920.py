'''
음계
숏코딩:
a=input()[2::2];print({a:"mixed","2345678":"ascending","7654321":"descending"}[a])
'''
input = input()
ascending = 0
descending = 0
for i in range(0,len(input.split(" "))-1):
    if int(input.split(" ")[i])-int(input.split(" ")[i+1]) == -1 :
        ascending += 1
    if int(input.split(" ")[i]) - int(input.split(" ")[i + 1]) == 1:
        descending += 1
if ascending == 7 :
    print("ascending")
elif descending == 7 :
    print("descending")
else :
    print("mixed")
