def solution(players, callings):
    result = {player: i for i, player in enumerate(players)} # 선수: 등수
    for i in callings:
        idx=result[i] #3
        result[i]-=1
        result[players[idx-1]]+=1
        players[idx], players[idx-1]=players[idx-1], players[idx]
    return players