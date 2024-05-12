# https://codeforces.com/contest/546/problem/A

k, n, w = [int(x) for x in input().split()]
 
money = (k*(w*(w+1)/2)-n)
 
if money > 0:
    print(int(money))
else:
    print(0)