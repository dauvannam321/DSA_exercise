# https://vjudge.net/problem/Kattis-guessthedatastructure
import heapq
import sys

for line in sys.stdin:
    n = int(line.strip())
    
    stack = []
    queue = []
    priority = []
    heapq.heapify(priority)

    isStack, isQueue, isPriority = True, True, True

    for _ in range(n):
        line = list(map(int, input().split()))

        if line[0] == 1:
            stack.append(line[1])
            queue.append(line[1])
            heapq.heappush(priority, -line[1])

        else:
            if isStack:
                if len(stack) == 0 or line[1] != stack[-1]:
                    isStack = False
                else:
                    stack.pop()

            if isQueue:
                if len(queue) == 0 or line[1] != queue[0]:
                    isQueue = False
                else:
                    queue.pop(0)

            if isPriority:
                if len(priority) == 0 or line[1] != -priority[0]:
                    isPriority = False
                else:
                    heapq.heappop(priority)

    if not isStack and not isQueue and not isPriority:
        print("impossible")
    elif (isStack and isQueue) or (isStack and isPriority) or (isQueue and isPriority):
        print("not sure")
    elif isStack:
        print("stack")
    elif isQueue:
        print("queue")
    elif isPriority:
        print("priority queue")