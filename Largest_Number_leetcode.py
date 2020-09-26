'''Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"


Example 2:

Input: [3,30,34,5,9]
Output: "9534330"   '''

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums)==0:
            return ''
        if all([v==0 for v in nums]):
            return '0'
        nums=list(map(str,nums))
        for x in range(len(nums)-1):
            y=x+1
            while y<len(nums):
                if (lambda x,y:int(x+y)>int(y+x))(nums[x],nums[y]):
                    pass
                else:
                    nums[x],nums[y]=nums[y],nums[x]
                y+=1
        return ''.join(nums)
