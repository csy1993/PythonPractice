'''
* @Author: csy 
* @Date: 2019-04-28 13:50:01 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:50:01 
'''
prompt = '\nPlease enter the name of a city you have visited:\n(Enter "quit" to exit.)\n'
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print('I like '+city + ',too.')
