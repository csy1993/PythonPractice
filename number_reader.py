'''
* @Author: csy 
* @Date: 2019-04-28 16:08:29 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 16:08:29 
'''
import json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers=json.load(f_obj)
print(numbers)