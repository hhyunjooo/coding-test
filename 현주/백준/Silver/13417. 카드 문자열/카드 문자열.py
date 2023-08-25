from collections import deque

t=int(input())

for _ in range(t):
    n=int(input())
    cards=deque(input().split())

    result=deque(cards.popleft())
    while(cards):
        number=cards.popleft()
        if number>result[0]:
            result.append(number)
        else:
            result.appendleft(number)
    print(''.join(result))