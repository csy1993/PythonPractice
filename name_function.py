'''
* @Author: csy 
* @Date: 2019-04-28 16:42:33 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 16:42:33 
'''
# def get_formatted_name(first,last):
#     '''生成整洁的名字'''
#     full_name=first+' '+last
#     return full_name.title()
# 
# def get_formatted_name(first,middle,last):
#     '''生成整洁的名字'''
#     full_name=first+' '+middle+' '+last
#     return full_name.title()
# 
def get_formatted_name(first,last,middle=''):
    '''生成整洁的名字'''
    if middle:
        full_name=first+' '+middle+' '+last
    else:
        full_name=first+' '+last
    return full_name.title()