'''
* @Author: csy 
* @Date: 2019-04-27 20:34:42 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-27 20:34:42 
'''


def build_person(first_name, last_name):
    '''返回一个字典，包含个人信息'''
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
