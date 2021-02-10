'''
* @Author: csy 
* @Date: 2019-04-28 13:50:29 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:50:29 
'''
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
#
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
