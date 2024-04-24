import sys

def normal_check(y, x):
    n_stack = [(y, x)]

    while n_stack:
        y, x = n_stack.pop()
        normal_check_list[y][x] = 1

        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]
            if 0 <= next_x < graph_size and 0 <= next_y < graph_size:
                if normal_color_list[next_y][next_x] == normal_color_list[y][x]:
                    if normal_check_list[next_y][next_x] == 0:
                        n_stack.append((next_y, next_x))


def patient_check(y, x):
    p_stack = [(y, x)]

    while p_stack:
        y, x = p_stack.pop()
        patient_check_list[y][x] = 1

        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]
            if 0 <= next_x < graph_size and 0 <= next_y < graph_size:
                if patient_color_list[next_y][next_x] == patient_color_list[y][x]:
                    if patient_check_list[next_y][next_x] == 0:
                        p_stack.append((next_y, next_x))

graph_size = int(sys.stdin.readline().strip())

normal_color_list = [[] for i in range(graph_size)]
patient_color_list = [[] for i in range(graph_size)]
normal_check_list = [[0]* graph_size for i in range(graph_size)]
patient_check_list = [[0]* graph_size for i in range(graph_size)]

normal_area_cnt, patient_area_cnt = 0, 0

for i in range(graph_size):
    colors = sys.stdin.readline().strip()
    for color in colors:
        normal_color_list[i].append(color)
        if color == 'G':
            color = 'R'
        patient_color_list[i].append(color)


dx, dy = [0,0,1,-1], [1,-1,0,0]

for i in range(graph_size):
    for j in range(graph_size):
        if normal_check_list[i][j] == 0:
            normal_check(i, j)
            normal_area_cnt += 1

        if patient_check_list[i][j] == 0:
            patient_check(i, j)
            patient_area_cnt += 1

sys.stdout.write(str(normal_area_cnt) + ' '+ str(patient_area_cnt))