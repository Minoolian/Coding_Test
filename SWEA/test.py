import bisect

group=[[[[[1,2,3] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]

a=[50]

print(bisect.bisect_left(a,150))
print(len(a)-bisect.bisect_left(a,150))

print(group[0][0][0][0])