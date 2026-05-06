class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1
        first_value = nums[0]
        last_value = nums[-1]

        if first_value <= last_value:
            return first_value
        if nums[0] > nums[-1] and nums[-1]< nums[-2]:
            return last_value 
        while l < r:
            mid = ((l+r)//2)

            if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                return nums[mid]
            elif first_value <= nums[mid]:
                l = mid+1
            else:
                r = mid
