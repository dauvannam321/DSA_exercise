import sys
class Scanner:
    def __init__(self, istream):
        self.tokenizer = Scanner.__tokenizer__(istream)
    def __tokenizer__(istream):
        for line in istream:
                for token in line.strip().split():
                        yield token
    def next(self):
        return self.tokenizer.__next__()

def count_pairs(arr, n, k):
    arr.sort()
    pairs = 0
    for i in range(n):
        left, right = i + 1, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if abs(arr[mid] - arr[i]) == k:
                pairs += 1
                break
            elif abs(arr[mid] - arr[i]) < k:
                left = mid + 1
            else:
                right = mid - 1
    return pairs

# Input
sc = Scanner(sys.stdin)
n = int(sc.next())
k = int(sc.next())
arr = []

for i in range(n):
    x = int(sc.next())
    arr.append(x)

# Output
print(count_pairs(arr, n, k))
