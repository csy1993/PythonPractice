'''
* @Author: csy 
* @Date: 2019-04-28 08:15:26 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 08:15:26 
'''


def greet_users(names):
    '''向列表中的每个用户发出简单问候'''
    for name in names:
        msg = 'Hello,'+name.title()
        print(msg)


usernames = ['hannah', 'try', 'margot']
greet_users(usernames)
