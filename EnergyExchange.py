# https://codeforces.com/problemset/problem/68/B

n, k = map(int, input().split())

amounts_energy = list(map(int, input().split()))

SumEnergy = sum(amounts_energy)
# print(SumEnergy)

l = min(amounts_energy)
r = max(amounts_energy)

mid = (l + r) / 2
while r - l > 1e-7:
    mid = (l + r) / 2
    SumTransfer = 0
    for i in amounts_energy:
        if i > mid:
            SumTransfer += i - mid
    SumLost = k/100 * SumTransfer

    if mid * n < (SumEnergy - SumLost): l = mid
    else: r = mid

print(mid)