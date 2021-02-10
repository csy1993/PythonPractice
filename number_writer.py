'''
* @Author: csy 
* @Date: 2019-04-28 16:06:34 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 16:06:34 
'''
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
