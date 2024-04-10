def solution(record):
    answer = []
    user = dict()
    actions = []
    for event in record:
        info = event.split()
        cmd,uid = info[0],info[1]
        if cmd != "Leave":
            nick = info[2]
            user[uid] = nick
        actions.append([cmd,uid])
    
    for action,uid in actions:
        if action == "Enter":
            answer.append(user[uid] + "님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(user[uid] + "님이 나갔습니다.")
    return answer