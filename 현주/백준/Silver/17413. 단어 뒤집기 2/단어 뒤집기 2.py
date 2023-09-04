import sys
s=sys.stdin.readline().strip() + ' '
how=0 #괄호 안인지
stack=[]
result=""
for i in s:
    if i=="<":
        how=1
        for _ in range(len(stack)): #괄호 만나기 이전 stack 애들 비워주고 다 뒤집어서 더해!
            result += stack.pop()
    stack.append(i)

    if i==">":
        how = 0 # 지금 괄호 빠져 나왔음 표시
        for _ in range(len(stack)): # 괄호 안에 있는 애들은 뒤집지 말고 더해!
            result += stack.pop(0)

    if i == ' ' and how == 0: # 공백을 만나고 괄호 밖에 있다면
        stack.pop() # 들어간 공백 뺴주고
        for _ in range(len(stack)): # 뒤집어서 더해!
            result += stack.pop()
        result += ' ' # 마지막에 공백 살려주기
print(result)