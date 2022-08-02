def solution(id_list, report, k):
    answer = []
    penalty_list = []
    user_dictonary = dict()
    penalty_dictonary = dict()
    reports = list(set(report))
    
    for repo in reports:
        r = repo.split()
        if r[0] not in user_dictonary:
            user_dictonary[r[0]] = [r[1]]
        else:
            temp = user_dictonary[r[0]]
            temp.append(r[1])
            user_dictonary[r[0]] = temp

        if r[1] not in penalty_dictonary:
            penalty_dictonary[r[1]] = 1
        else:
            penalty_dictonary[r[1]] += 1    
    
    for key, value in penalty_dictonary.items():
        if value >= k:
            penalty_list.append(key)
    
    if not penalty_list:
        return [0 for _ in range(len(id_list))]
    
    for user_id in id_list:
        cnt = 0
        for name in penalty_list:
            if user_dictonary.get(user_id) == None:
                break
            else:
                if name in user_dictonary[user_id]:
                    cnt += 1
        answer.append(cnt)
    return answer