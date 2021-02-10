'''
* @Author: csy 
* @Date: 2019-04-28 13:50:19 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:50:19 
'''
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user:'+current_user.title())
    confirmed_users.append(current_user)
print('\nThe following user have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
