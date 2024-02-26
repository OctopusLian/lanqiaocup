import os
import sys
n=int(input())   #接受用户输入的一个整数，并将其赋值给变量n
k={}       #创建一个空字典
for i  in range(n):
  x=int(input())
  if x in k.keys():
    k[x]+=1
  else:
    k[x]=1
a=list(k.keys())
a.sort()
for i in a:
  print(i,k[i])