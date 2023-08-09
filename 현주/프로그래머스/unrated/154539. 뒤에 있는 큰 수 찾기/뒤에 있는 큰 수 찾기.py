def solution(numbers):
    answer = []
    stack = [] #0
    answer = [-1 for i in range(len(numbers))]
    for i, ele in enumerate(numbers): # 0, 2
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i) 
    return answer