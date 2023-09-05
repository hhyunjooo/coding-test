def solution(keymap, targets):
    answer = []
    
    output_list = [] # [['A', 'B', 'A', 'C', 'D'], ['B', 'C', 'E', 'F', 'D']]

    for string in targets:
        char_list = list(string)
        output_list.append(char_list)

    keytable = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in keytable:
                keytable[key] = i + 1
            else:
                keytable[key] = min(keytable[key], i + 1) #{'A': 1, 'B': 1, 'C': 2, 'D': 5, 'E': 3, 'F': 4}
    for j in output_list: #['A', 'B', 'A', 'C', 'D']
        num=0
        for z in j:
            if z in keytable:
                num+=keytable[z]
            else:
                num=-1
                break
        answer.append(num)
        
    return answer