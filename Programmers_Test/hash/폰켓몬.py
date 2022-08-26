def solution(nums):
    answer = 0
    temp = len(set(nums))
    max_number = len(nums) // 2
    answer = temp if max_number > temp else max_number
    return answer