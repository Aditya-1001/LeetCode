class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,val in enumerate(nums):
            if val not in dic:
                dic[target-val]=i
            else:
                return {i,dic[val]}
            
            
