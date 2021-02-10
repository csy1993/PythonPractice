'''
* @Author: csy 
* @Date: 2019-04-28 16:19:12 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 16:19:12 
'''
import json
filename = 'username.json'
with open(filename) as f_obj:
    username=json.load(f_obj)
    print('Welcome back,'+username.title())