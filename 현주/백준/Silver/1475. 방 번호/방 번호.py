arr=[0]*10
n=list(input())
for i in range(len(n)):
    if n[i]=='6' or n[i]=='9':
        if arr[6] <= arr[9]:
            arr[6]+=1
        else:
            arr[9]+=1
    else:
        arr[int(n[i])]+=1
print(max(arr))