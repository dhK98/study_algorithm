def solution(participant, completion):
    list_up = dict()
    for p in participant:
        list_up[p] = list_up.get(p,0) + 1
    for c in completion:
        list_up[c] = list_up.get(c,0) - 1
        
    return [people for people in list_up if list_up[people] > 0] [0]
 