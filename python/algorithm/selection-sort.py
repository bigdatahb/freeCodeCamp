"""
选择排序:
    每次从未排序的数中选择一个最小的放在未排序的第一个位置
"""

def selection_sort(array):
    if not array:
        return array
    first_index = 0
    while first_index < len(array):
        # find the min value index
        min_index = first_index
        min_value = array[first_index]
        # 一定要注意这里循环的开始索引位置要保持和原数组一致， enumerate 第二个参数指定
        for index, value in enumerate(array[first_index + 1:], first_index + 1):
            if value < min_value:
                min_value = value
                min_index = index

        if min_index > first_index:
            # swap
            array[first_index], array[min_index] = array[min_index], array[first_index]

        # first_index move forward 1
        first_index += 1

    return array

print(selection_sort([33, 1, 89, 2, 67, 245]))

arr = [1, 2, 3, 4]
arr[0], arr[1] = arr[1], arr[0]
print(arr)
