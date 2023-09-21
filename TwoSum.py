
# Online Python - IDE, Editor, Compiler, Interpreter
nums= [1,5,8,9,16,19]
Target= 14
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]