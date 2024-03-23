import heapq

def solution(operations):
    order_list = [0] * len(operations)
    num_list = []
    
    for i in range(len(operations)):
        order_list[i] = operations[i].split()
    
    for i in range(len(order_list)):
        if order_list[i][0] == 'I':
            heapq.heappush(num_list, int(order_list[i][1]))
            
        else:
            if order_list[i][1] == '-1':
                if len(num_list) != 0:
                    heapq.heappop(num_list)
            
            else:
                if len(num_list) != 0:
                    num_list.remove(max(num_list))
                    
    
    if len(num_list) == 0:
        answer = [0, 0]
    else:
        answer = [max(num_list), heapq.heappop(num_list)]
                
    return answer