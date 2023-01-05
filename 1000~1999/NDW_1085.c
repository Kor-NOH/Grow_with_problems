lst = []

a, b, c, d= input("").split()

case_1 = int(a) - 0
case_2 = int(a) - int(c)
case_3 = int(b) - 0
case_4 = int(b) - int(d)

lst.append(abs(case_1))
lst.append(abs(case_2))
lst.append(abs(case_3))
lst.append(abs(case_4))
lst.sort()

print(lst[0])