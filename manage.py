写一个删除列表中重复元素的函数，要求去重后元素相对位置保持不变。


def dedup(items):
    no_dup_items = []
    seen = set()
    for item in items:
        if item not in seen:
            no_dup_items.append(item)
            seen.add(item)
    return no_dup_items
