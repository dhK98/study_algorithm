import sys
sys.setrecursionlimit(2000)

# 효율성 통과안됨
def solution(k, room_number):
    answer = []
    check_room = dict()
    index = 0
    how_much_reapt = 0
    while index < len(room_number):
        wanted_room_number = room_number[index] + how_much_reapt
        if wanted_room_number not in check_room:
            check_room[wanted_room_number] = wanted_room_number + 1
            answer.append(wanted_room_number)
            index += 1
            how_much_reapt = 0
        else:
            how_much_reapt += 1 
    return answer

# 정석 풀이
import sys
sys.setrecursionlimit(2000)

def solution(k, room_number):
    rooms = dict()
    for num in room_number:
        chk_in = find_emptyroom(num,rooms)
    return list(rooms)


def find_emptyroom(chk,rooms):
    if chk not in rooms:
        rooms[chk] = chk + 1
        return chk
    empty = find_emptyroom(rooms[chk],rooms)
    rooms[chk] = empty + 1
    return empty
