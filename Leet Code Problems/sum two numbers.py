'''
leetcode.com
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up 
to target.
You may assume that each input would have exactly one 
solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
'''
def twosum(list1, target):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if i != j:
                if target == list1[i] + list1[j]:
                    print(f"{list1[i]} and {list1[j]}")
                    print(f"{i} and {j}")
                    a,b = i, j
            j += 1
        i += 1
    return a, b

list1 = [2, 7, 11, 15, -2]
target = 9

c = twosum(list1, target)
#print(f"{list1[a]} and {list1[b]}")




#Do this way
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
'''