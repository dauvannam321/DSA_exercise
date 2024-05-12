#  https://vjudge.net/problem/SPOJ-PQUEUE
#  cheezepham's solution for [SPOJ-PQUEUE]

t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))

    jobs = list(map(int, input().split()))
    # print(jobs)

    q = []

    for i in range(n):
        q.append((jobs[i], i))

    time = 0
    while q:
        mx = max(q)
        if mx[0] == q[0][0]:
            time += 1
            if q[0][1] == m:
                print(time)
                break
            q.pop(0)

        else:
            q.append(q.pop(0))