'''
* @Author: csy 
* @Date: 2019-04-28 08:29:19 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 08:29:19 
'''
# unprinted_designs=['iphone case','robot pendant','dodecahedron']
# completed_models=[]
# while unprinted_designs:
#     current_design=unprinted_designs.pop()
#     print('Printing model: '+current_design)
#     completed_models.append(current_design)
# print('\nThe following models have been printed:')
# for completed_model in completed_models:
#     print(completed_model)
#


def print_models(unprinted_designs, completed_models):
    '''模拟打印每个设计，直到没有未打印的为止。打印每个设计后，移动到列表completed_models'''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model: '+current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    '''显示打印好的所有模型'''
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
