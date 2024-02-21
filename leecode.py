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

#14
class Solution:
    def romanToInt(self, s: str) -> int:
        end=0
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if 'IX' in s:
            s=s.replace('IX','')   
            end +=9
        if 'IV' in s:
            s=s.replace('IV','')
            end+=4
        if 'XL'in s:
            s=s.replace('XL','')
            end+=40
        if 'XC' in s:
            s=s.replace('XC','')
            end+=90
        if 'CD' in s:
            s=s.replace('CD','')
            end +=400
        if 'CM' in s:
            s=s.replace('CM','')
            end+=900       
        for i in s:
                end+=dic[i]        
        return end
'''
#20
strs = ["flower","flow","flight"]
minLen = min(len(s) for s in strs)
strs[1]
#print(strs[0][:2])
a = 0
for i in range(0,minLen-1):
    for j in range(0,len(strs)-1):
        print(strs[1])
        if strs[0][i] != strs[j][i]:
            a = i
            print(i)
            break
#print(strs[0][:0])