from functools import reduce

numbers=[0,0,0,0,0]


res=print([(x,numbers[x]) for x in range(1,len(numbers)-1) if sum(numbers[:x])==sum(numbers[x+1:])])

print(list(filter(lambda x:sum(numbers[:x])==sum(numbers[x+1:]),range(1,len(numbers)-1))))