# https://codeforces.com/problemset/problem/520/A
n = int(input())
sentences = input().upper()
dict = {}
for i in range(26):
    dict[chr(i + 65)] = 0

for i in sentences:
    dict[i] += 1
if 0 in dict.values():
    print("NO")
else:
    print("YES")
