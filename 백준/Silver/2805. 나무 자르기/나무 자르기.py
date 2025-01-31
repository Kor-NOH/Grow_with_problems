import sys

def wood_amount(trees, height):
    return sum(max(0, tree - height) for tree in trees)

def find_max_height(n, m, trees):
    low, high = 0, max(trees)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if wood_amount(trees, mid) >= m:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result

# 입력 받기
n, m = map(int, input().split())  # 또는 sys.stdin.readline().strip().split()
trees = list(map(int, input().split()))  # 또는 sys.stdin.readline().strip().split()

# 결과 출력
print(find_max_height(n, m, trees))
