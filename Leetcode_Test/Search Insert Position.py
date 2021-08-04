class Solution:
    def binary_search(sorted_list, search):
        left = 0
        right = len(sorted_list)-1

        while(left <= right):
            ## middle은 left와 right의 중간지점
            middle = (left+right)//2
            
            ## search가 list[middle]보다 작다. right = middle-1
            if search < sorted_list[middle]:
                right = middle - 1
            
            ## search가 list[middle]보다 크다. left = middle+1
            elif sorted_list[middle] < search:
                left = middle + 1
            
            ## search가 list[middle]과 같다. 인덱스 반환
            else:
                return middle
            
        ## while문을 빠져나오는 경우 : right < left
        ## 즉, 리스트 안에 search가 존재하지 않는다
        return -1

    def searchInsert(self, nums: List[int], target: int) -> int:
        answer =  Solution.binary_search(nums,target)
        
        if answer == -1:
            if nums[0] > target:
                return 0
            elif nums[len(nums)-1] < target:
                return len(nums)
            else: #사이에 낀 친구들
                for index in range(len(nums)):
                    if nums[index] > target:
                        return index
        else:
            return answer