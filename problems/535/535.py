"""
统计数字
"""

n = int(input())
nums = {}
for i in range(n):
    x = int(input())
    if x in nums.keys():
        nums[x] += 1
    else:
        nums[x] = 1
key = list(nums.keys())
key.sort()
for i in key:
    print(i, nums[i])
