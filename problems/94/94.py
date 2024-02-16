num = int(input())  #卡片数目
arr = input()  #顺时针排列的卡片
result = 0  #存答案，赢得球票数字之和
for i in range(num):          #用i的变化表示从哪里开始数
    pocket = 0  #赢来的球票数目
    nums = 1   #计数器初始化
    numarr = list(map(int,arr.split()))    #初始化arr列表于int类型
    while(numarr and nums<=max(numarr)):
        if numarr[i]==nums:
            pocket+=numarr.pop(i)
            nums = 1
            if len(numarr) == 0:
                break
            i = i%len(numarr)   #循环队列头尾
        else:
            nums+=1
            i = (i+1)%len(numarr)
    if pocket>result:
        result = pocket
print(result)