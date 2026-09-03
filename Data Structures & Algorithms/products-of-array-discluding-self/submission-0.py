class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right =len(nums)-1
        leftArray, RightArray = [1] * len(nums), [1] * len(nums)
        leftTotal, rightTtotal =1, 1
        for left in range(len(nums)):
            if left-1 >= 0:
                leftArray[left] = leftTotal * nums[left-1]
                leftTotal = leftTotal * nums[left-1]
            else:
                leftArray[left] = leftTotal 
            if right+1 < len(nums):
                RightArray[right] = rightTtotal * nums[right+1] 
                rightTtotal= rightTtotal * nums[right+1]
            else:
                RightArray[right]  = rightTtotal
            right-=1
        results = [x * y for x, y in zip(leftArray, RightArray)]
        return results

        