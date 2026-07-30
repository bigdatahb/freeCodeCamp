"""
快速排序
"""

def quick_sort(array):
    """
    快速排序主要思想:
        1. 随机选择一个 key (数组的第一个或最后一个元素）
        2. 将数组分为 3 个部分： 元素值小于 key 的部分， 元素值等于 key 的部分, 元素值大于 key 的部分
        3. 递归使用快速排序对 3 个部分进行排序
        4. 拼接 3 个部分排序后的结果，形成最终结果
    :param array: 要排序的数组
    :return: 排好序的新数组
    """
    if not array:
        return []  # 对于空数组直接返回 空数组
    key = array[0] # 取第一个元素作为 key
    left = [e for e in array if e < key]  # 用来保存元素值小于 key 的部分
    right = [e for e in array if e > key] # 用来保存元素值大于 key 的部分
    keys = [e for e in array if e == key] # 用来保存元素值等于 key 的部分

    # 如果没有 大于 key 的元素也没有小于 key 的元素，说明所有元素都等于 key, 直接返回 keys
    if not left and not right:
        return keys

    if left:
        # 如果有小于 key 的子数组, 对其使用快速排序
        sorted_left = quick_sort(left)
    else:
        sorted_left = []
    if right:
        # 如果有大于 key 的子数组, 对其使用快速排序
        sorted_right = quick_sort(right)
    else:
        sorted_right = []

    # 拼接排序好的各部分子数组， 形成最终排序结果并返回
    return sorted_left + keys + sorted_right


print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))
