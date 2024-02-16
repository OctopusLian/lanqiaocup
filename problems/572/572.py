"""
火星人
"""

n = int(input())
m = int(input())
nums = list(map(int, input().split()))


def find_next(nums):
    for i in range(n - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            for j in range(n - 1, i - 1, -1):
                if nums[j] > nums[i - 1]:
                    nums[j], nums[i - 1] = nums[i - 1], nums[j]
                    return nums[:i] + nums[:i - 1:-1]


for i in range(m):
    nums = find_next(nums)  # 找后面第m个排列
print(" ".join([str(i) for i in nums]))
