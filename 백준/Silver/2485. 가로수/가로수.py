import sys
import math
import heapq

test_cnt = int(sys.stdin.readline())
tree_bet_dis = []
tree_cnt, past = 0, 0
add_tree_cnt = 0

for _ in range(test_cnt):
    tree = int(sys.stdin.readline())
    if tree_cnt != 0:
        tree_bet_dis.append(tree - past)
    tree_cnt += 1
    past = tree

goal = heapq.heappop(tree_bet_dis)
div = goal
for i in range(len(tree_bet_dis)):
    div = math.gcd(div, tree_bet_dis[i])

heapq.heappush(tree_bet_dis, goal)

for tree in tree_bet_dis:
    add_tree_cnt += tree // div - 1

sys.stdout.write(str(add_tree_cnt))