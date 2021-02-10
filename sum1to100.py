'''
* @Author: csy 
* @Date: 2019-04-28 13:57:50 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:57:50 
'''
#!/usr/bin/env python3
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum))
