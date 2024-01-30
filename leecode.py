'''
#1.1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(0,l):
            for j in range(i+1,l):
                if nums[i] + nums[j] == target:
                    return [i,j] 
#1.2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

#9
class Solution:
    def isPalindrome(self, x: int) -> bool:
        b = str(x)[::-1]
        if b == str(x):
            return True
        else:
            return False

'''
s = '1231I'
b = str(s)[::-1]
num = 0
for i in b:
    if i is 'I':
        num = num + 1
    if i
