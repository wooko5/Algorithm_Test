def solution(data, ext, val_ext, sort_by):
    criteria = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    ext_criterion = criteria[ext]
    sort_criterion = criteria[sort_by]
    result = []

    for index in range(len(data)):
        if data[index][ext_criterion] < val_ext:
            result.append(data[index])

    return sorted(result, key=lambda x: x[sort_criterion])



data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"
# result = [[3,20300401,10,8],[1,20300104,100,80]]
print(solution(data, ext, val_ext, sort_by))