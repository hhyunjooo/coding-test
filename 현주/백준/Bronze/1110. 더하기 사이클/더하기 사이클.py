n=int(input())
result=""
new=n
sum=0
if n<10:
    n=int("0"+str(n))
while True:
    # n=str(n%10)+str((n//10+n%10)%10)
    n=int(str(n%10)+  str((n//10+n%10)%10))
    sum+=1

    if n==new:
        break
print(sum)