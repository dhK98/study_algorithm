def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)
    for skill_tree in skill_trees:
        stack = []
        for string in skill_tree:
            if string in skill_list:
                stack.append(string)
        if not stack or skill.startswith(''.join(stack)):
            answer +=1
    return answer