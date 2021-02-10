'''
* @Author: csy 
* @Date: 2019-04-28 13:55:57 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:55:57 
'''
responses = {}
polling_active = True
while polling_active:
    name = input('\nWhat is your name?')
    response = input('Which mountain would you like to climb someday?')
    responses[name] = response
    repeat = input('Would you linke to let another person respond?(yes/ no)')
    if repeat == 'no':
        polling_active = False
print('\n---Poll Results ---')
for name, response in responses.items():
    print(name+'Would linke to climb '+response)
