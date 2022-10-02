def solution(nums):
    answer = 0
    temp = len(set(nums))
    max_number = len(nums) // 2
    answer = temp if max_number > temp else max_number
    return answer

# 2022.10.02 다시 풀음
def solution(nums):
    size = len(set(nums))
    if len(nums)//2 <= size:
        return len(nums)//2
    return size