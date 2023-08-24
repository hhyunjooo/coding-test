n=int(input())
arr=[]
for _ in range(n):
    num=int(input())
    arr.append(num)

dp=[0]*n
if len(arr)<=2:
    print(sum(arr))
else:
    dp[0]=arr[0]
    dp[1]=arr[0]+arr[1]
    for i in range(2, n): #3~n
        dp[i]=max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i]) #2계단 연속(3계단 연속은 안되므로 dp[i-3]), 1계단 건너뜀
    print(dp[-1])