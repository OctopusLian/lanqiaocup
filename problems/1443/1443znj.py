
num=0  #用num来累计用过的数字“1”的次数
for i in range(1,10000):
       num+=str(i).count("1")  #出现过几次1就 给num加上多少
       if num>2021:  #当num数量超过2021时卡牌数量不足
              break
print(i-1)