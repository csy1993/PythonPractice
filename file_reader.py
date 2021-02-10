'''
* @Author: csy 
* @Date: 2019-04-28 13:47:18 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:47:18 
'''
# with open('./pi_digits.txt') as file_object:
#     contents=file_object.read()
#     print(contents)
#     print(contents.rstrip())  #删除末尾空白
#
# filename='pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line)
#
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)
for line in lines:
    print(line)
