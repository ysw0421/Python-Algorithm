'''
알파벳 찾기
숏코딩:
print(*map(input().find,map(chr,range(97,123))))
'''
Word = input()
List = []
Set = set()
for i in  range(0,26):
    List.append(-1)
location = 0
for word in Word:
    if word not in Set:
        Set.add(word)
        List[ord(word)-97] = location
    location += 1
for i in  range(0,26):
    print (List[i], end=" ")
