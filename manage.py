要求：列表中有1000000个元素，取值范围是[1000, 10000)，设计一个函数找出列表中的重复元素。


import random


def find_duplicate(items: list):
    dups = [0] * 9000
    for item in items:
        dups[item - 1000] += 1
    for idx, val in enumerate(dups):
        if val > 1:
            yield idx + 1000


lst = [random.randint(1000, 9999) for _ in range(1000000)]
duplicates = find_duplicate(lst)
print(duplicates)
for i in duplicates:
    print(i)
    
：这道题的解法和计数排序的原理一致，虽然元素的数量非常多，
但是取值范围[1000, 10000)并不是很大，只有9000个可能的取值，
所以可以用一个能够保存9000个元素的dups列表来记录每个元素出现的次数，
dups列表所有元素的初始值都是0，通过对items列表中元素的遍历，当出现某个元素时
，将dups列表对应位置的值加1，最后dups列表中值大于1的元素对应的就是items列表中重复出现过的元素。

