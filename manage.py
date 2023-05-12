from collections import Counter
nums = [1,2,3,3,3,2]
count = Counter(nums)
print(count)
'''
输出
Counter({3: 3, 2: 2, 1: 1})
'''

print(count[3]) # 打印3的个数
'''
输出
3
'''

for k,v in count.items():
    print(k,v)
'''
输出
1 1
2 2
3 3
'''

a = count.most_common(2)
print(a)
'''
输出
[(3, 3), (2, 2)]
'''

print([1,2,3].count(1))

