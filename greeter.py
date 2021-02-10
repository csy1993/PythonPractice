'''
* @Author: csy 
* @Date: 2019-04-27 08:55:05 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-27 08:55:05 
'''
# print('Hello,'+input('Please input your name:'))
#
# def greet_user():
#     """显示简单的问候语"""
#     print('Hello!')
# greet_user()
#
# def greet_user(username):
#     '''向用户问好'''
#     print('Hello,'+username)
# greet_user('CSY')
#


def get_formatted_name(first_name, last_name):
    '''返回整洁名字'''
    full_name = first_name+' '+last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print('(Enter "q" to quit)')
    f_name = input('First name:\t')
    if f_name == 'q':
        break
    l_name = input('Last name:\t')
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello,'+formatted_name)
