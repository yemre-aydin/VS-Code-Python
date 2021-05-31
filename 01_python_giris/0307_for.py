"""
for i in range(5):


sayiDizisi=list(range(10))
"""

"""
[1 x 1 = 1]	[1 x 2 = 2]	[1 x 3 = 3]	[1 x 4 = 4]	[1 x 5 = 1]
[2 x 1 = 2]	[2 x 2 = 4]	[2 x 3 = 6]	[2 x 4 = 8]	[2 x 5 = 10]
...
[5 x 1 = 5]	[5 x 2 = 10]	[5 x 3 = 15]	[5 x 4 = 20]	[5 x 5 = 25]
"""

for i in range(1,6):
    for j in range(1,6):
        print(f"[{i} x {j} = {i*j}] ",end=" ")
    print()
