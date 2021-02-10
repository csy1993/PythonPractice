'''
* @Author: csy 
* @Date: 2019-04-28 13:53:06 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:53:06 
'''
# 斐波那契(fibonacci)数列模块


def fib(n):    # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n):  # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
