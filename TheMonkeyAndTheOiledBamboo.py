# https://vjudge.net/problem/UVA-12032

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    r = list(map(int, input().split()))

    rungs = [r[0]]
    for i in range(1, len(r)):
        rungs.append(abs(r[i]-r[i-1]))

    maxR = max(rungs)
    res = maxR

    for i in rungs:
        if i == maxR:
            maxR -= 1
        elif i > maxR:
            res += 1
            break

    print("Case {}: {}".format(t, res))


'''
2
5
1 6 7 11 13
4
3 9 10 14
'''