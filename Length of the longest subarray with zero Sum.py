
#Brute Force Approach to find the length of the longest subarray with zero sum
#Time Complexity: O(n^2)
#Space Complexity: O(1)
def SubarrayWithZeroSum(nums):
    max_Length = 0
    for i in range(len(nums)):
        sum = nums[i]
        for j in range(i+1,len(nums)):
            sum += nums[j]
            if sum == 0:
                max_Length = max(max_Length, j-i+1)
    return max_Length

nums = [9, -3, 3, -1, 6, -5]
nums = [6, -2, 2, -8, 1, 7, 4, -10]
nums = [1, 3, -5, 6, -2]
print(SubarrayWithZeroSum(nums))

#Optimal Approach using HashMap
#Time Complexity: O(n)
#Space Complexity: O(n)
def SubarrayWithZeroSumOptimal(nums):
    max_count = 0
    dict1 = {}
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum == 0:
            max_count = i+1
        if sum not in dict1:
            dict1.update({sum:i})
        elif sum in dict1:
            max_count = max(max_count,i- dict1[sum]) 
    return max_count
nums = [1, 3, -5, 6, -2]
nums = [6, -2, 2, -8, 1, 7, 4, -10]
print(SubarrayWithZeroSumOptimal(nums))
