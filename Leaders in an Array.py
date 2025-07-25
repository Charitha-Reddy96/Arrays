
'''You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.

Examples:

Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.

'''

import math
class Solution:
    def leaders(self, arr):
        maxi = arr[-1]
        nums = [maxi]
        for i in range(len(arr)-2,-1,-1):
             if maxi <= arr[i]:
                 nums.append(arr[i])
                 maxi = arr[i]
        return reversed(nums)
             
#Time Complexity: O(n)
#Space Complexity: O(n)