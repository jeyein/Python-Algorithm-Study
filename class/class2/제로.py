#https://www.acmicpc.net/problem/10773

import sys
input = sys.stdin.readline

k = int(input())
arr = []

for i in range(k):
    num = int(input())


    if num == 0:
        arr.pop()
    else:
        arr.append(num)

print(sum(arr))