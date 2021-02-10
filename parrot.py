'''
* @Author: csy 
* @Date: 2019-04-28 13:56:30 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:56:30 
'''
# print(input('Tell me somethin,and I will back the same to you:'))
#
prompt = "Say something,if you want to out,please enter 'quit':"
#
#  message=''
# while message != 'quit':
#     message=input(prompt)
#     if message != 'quit':
#         print(message)
#
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
