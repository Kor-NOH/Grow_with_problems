arr = []
high = 0
location = 0
for i in range(9):
    a = int(input())
    arr.append(a)

for i in range(9):
    if arr[i] > high:
        high = arr[i]
        location = i+1

print(high)
print(location)