"""
This just generates a random list of integers from 1-10,000 that is 1000 items long.
OpenHash testing uses the list this generates, called randomlist
"""

import random
randlist = []

for i in range(0,1000):
    randlist.append(random.randint(1,10000))

f = open("randomlist", "w")
f.write("\n".join(map(lambda x: str(x), randlist)))
f.close()
print('new random list created.')
