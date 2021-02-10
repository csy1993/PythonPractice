'''
* @Author: csy 
* @Date: 2019-04-28 16:10:36 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 16:10:36 
'''
# import json
# username = input("What is your name?")
# filename = 'username.json'
# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print("We will remember you when you come back,"+username.title())
#
# import json

# filename = 'username.json'
# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input("What's your name?")
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         print("We'll remember you when you come back,"+username.title())
# else:
#     print('Welcome back,'+username.title())
# import json

# def greet_user():
#     '''问候用户，并指出名字'''
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input("What's your name?")
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj)
#             print("We'll remember you when you come back,"+username.title())
#     else:
#         print('Welcome back,'+username.title())
# greet_user()
# 
import json
def get_stired_username():
    ''''如果存储了用户名，就获取它'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    '''提示用户输入用户名'''
    username = input("What's your name?")
    filename='username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
def greet_user():
    '''问候用户，并指出名字'''
    username = get_stired_username()
    if username:
        print('Welcome back,'+username.title())
    else:
        username=get_new_username()
        print("We'll remember you when you come back,"+username.title())
greet_user()