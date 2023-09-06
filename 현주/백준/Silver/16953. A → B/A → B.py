a,b = map(int, input().split())
count=0
while (a<b):
    if(b%2==0):
        count+=1
        b=b//2
    elif str(b)[-1]=="1":
        count+=1
        if len(str(b))>1:
            b=int(str(b)[:-1])
        else:
            break
    else:
        break
if(a==b):
    print(count+1)
else:
    print(-1)