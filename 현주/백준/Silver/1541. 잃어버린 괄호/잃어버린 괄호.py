exp = input().split('-') #'-'를 기준으로 split해서 exp 리스트에 저장 009, 009

num = [] #'-'로 나눈 항들의 합을 저장할 리스트
for i in exp:
    sum=0
    plus=i.split("+")
    for p in plus:
        sum+=int(p)
    num.append(sum)

n=num[0]
for a in range(1, len(num)):
    n-=num[a]
print(n)