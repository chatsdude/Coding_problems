 '''Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.'''
 def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums) < 3):
            return len(nums)
        i = 1    
        for j in range(2, len(nums)):
            if (nums[i-1] != nums[j]) or (nums[i] != nums[j]):
                i += 1        
            nums[i] = nums[j]   
        return i+1