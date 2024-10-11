print("Hello, Python world")
a = 10
b = 0.000001
c = 'string'
print(a, b, c)

for x in {1, 2, 3}:
    print(x)
    if x == 2:
        break   
n = 10 
for i in range(n):
     print(i)
     if i == 5:
         break
     
     
import math
print()
print(math.pi)

from sort import quick_sort

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
sorted_data = quick_sort(data.copy()) 
print(f"ソート結果: {sorted_data}")

from rsp import rsp
rsp()
