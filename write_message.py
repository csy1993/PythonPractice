'''
* @Author: csy 
* @Date: 2019-04-28 14:49:35 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 14:49:35 
'''
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write('I love creating new games.\n')
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets\n")
    file_object.write('I love creating apps that can run in a browser.\n')
