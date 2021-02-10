'''
* @Author: csy 
* @Date: 2019-04-28 13:55:42 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:55:42 
'''
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}
for username, userinfo in users.items():
    print('Username:'+username.title())
    print('\tFullname:'+userinfo['first']+'\t'+userinfo['last'])
    print('\tLocation:'+userinfo['location'])
    print()
