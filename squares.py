'''
* @Author: csy 
* @Date: 2019-04-28 13:57:43 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:57:43 
'''
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)
