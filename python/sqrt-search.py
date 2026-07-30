"""
使用二分查找法来搜索一个正整数的平方根，可以设置误差精度以及迭代次数

我记得考试的时候精度有点问题总是通不过测试，我是将 tolerance /= 10 才通过的，这里没有体现
"""

def square_root_bisection(value, tolerance=0.01, max_iter=5):
    if value < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    if value == 0 or value == 1:
        print(f'The square root of {value} is {value}')
        return value

    if value > 1:
        low = 1
        high = value
    else:
        low = value
        high = 1

    iter_cnt = 0
    while low <= high:
        iter_cnt += 1
        if iter_cnt > max_iter:
            break
        mid = (low + high) / 2
        if (value < mid ** 2 and mid ** 2 - value <= tolerance) or (value > mid ** 2 and value - mid ** 2 <= tolerance):
            print(value, mid**2)
            print(f'The square root of {value} is approximately {mid}')
            return mid
        if mid ** 2 < value:
            low = mid
        else:
            high = mid

    print('Failed to converge within [maximum] iterations')
    return None


square_root_bisection(0.001, 1e-8, 50)


