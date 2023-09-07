t=int(input())
for _ in range(t):
    n ,m =map(int, input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    answer = 0
    cnt=0
    a.sort()
    b.sort()
    for i in a:
        if i>b[0]:
            left = 0 
            right = m-1
            result=0

            while left <= right: #136
                mid = (left + right) // 2
                if b[mid] < i:
                    result = mid  # mid까지의 원소는 모두 i보다 작음
                    left = mid + 1
                else:
                    right = mid - 1
            result+=1
            answer+=result
    print(answer)