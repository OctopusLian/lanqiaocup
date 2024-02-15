"""
拼数
"""

n = int(input())
nums = input().split()
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if nums[j] + nums[i] > nums[i] + nums[j]:
            nums[j], nums[i] = nums[i], nums[j]  # 交换两个数的位置
print(''.join(nums))
