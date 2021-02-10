'''
 * @Author: csy 
 * @Date: 2019-04-27 20:24:27 
 * @Last Modified by:   csy 
 * @Last Modified time: 2019-04-27 20:24:27 
 '''


def get_formatted_name(first_name, last_name):
    '''返回整洁名字'''
    full_name = first_name+' '+last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
