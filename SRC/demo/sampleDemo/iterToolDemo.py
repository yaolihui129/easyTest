import itertools
from pprint import pprint

# horses = [1, 2, 3, 4,5,6]
# races = itertools.permutations(horses)
# print(races)
# pprint(list(itertools.permutations(horses)))


# res=itertools.count(10, 2)
# print(res)
# print(type(res))
# for x in res:
# 	print(x)
# 	if x>100:
# 		break

# res=itertools.cycle('abc')
# for x in res:
# 	print(x)


# res=itertools.repeat(5,10)
# for x in res:
# 	print(x)


for m, n in itertools.product('abc', [1, 2]):
    print(m,n)