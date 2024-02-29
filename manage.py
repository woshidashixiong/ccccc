python实现快速排序算法

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# 示例
sorted_arr = quick_sort([34,67,12,6,8,23,56,90])
print(sorted_arr)

这段代码定义了一个 quick_sort 函数，该函数接受一个数组作为输入，并返回排序后的新数组。具体实现步骤如下：

如果输入数组长度小于等于1，直接返回。
选择数组的第一个元素作为基准元素（pivot）。
将数组中比基准元素小的元素放到一个新数组 less_than_pivot 中。
将数组中比基准元素大的元素放到一个新数组 greater_than_pivot 中。
递归地对 less_than_pivot 和 greater_than_pivot 进行快速排序。
将排序后的 less_than_pivot、基准元素、greater_than_pivot 拼接在一起返回。
