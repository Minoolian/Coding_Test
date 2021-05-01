from itertools import permutations
from collections import Counter

a=['+','-','*','-']

b=Counter(a)


for i in permutations(b.keys(),len(b.keys())):
    print(i)