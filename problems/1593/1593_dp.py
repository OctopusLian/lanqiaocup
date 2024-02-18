"""
https://www.lanqiao.cn/problems/1593/learning/?page=1&first_category_id=1&name=%E4%BA%8C%E8%BF%9B%E5%88%B6%E9%97%AE%E9%A2%98
二进制问题
"""

N = 60
dp = [[0] * N for i in range(N)]
for i in range(N):  # 计算组合数
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
r, k = map(int, input().split())
nums = str(bin(r))[2:]  # 转化为二进制，存在nums[]中
ans = 0
for i in range(0, len(nums)):  # 从高位到低位，nums[0]是二进制最高位
    if nums[i] == '1':
        plus = int(dp[len(nums) - i - 1][k])
        ans += plus
        if plus == 0:
            if int(nums[i]) == k:  ans += 1  # 二进制数最后一位正好==k值
            break
        k -= 1
print(ans)
