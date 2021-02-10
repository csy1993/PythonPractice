'''
* @Author: csy 
* @Date: 2019-04-28 08:29:11 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 08:29:11 
'''
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese']
# }
# print('You order a '+pizza['crust'] +'-crust pizza with the following toppings:')
# for topping in pizza['toppings']:
#     print('\t' + topping)
#
# def make_pizza(*toppings):
#     '''打印顾客点的所有配料'''
#     print('Following toppings:')
#     for topping in toppings:
#         print('\t-'+topping.title())
# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')
#
# def make_pizza(size,*toppings):
#     '''概述要做的披萨'''
#     print('Make a '+str(size)+'-inch pizza with the following toppings:')
#     for topping in toppings:
#         print('\t-'+topping.title())
# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','green peppers','extra cheese')
#


def make_pizza(size, *toppings):
    '''概述要做的披萨'''
    print('Make a '+str(size)+'-inch pizza with the following toppings:')
    for topping in toppings:
        print('\t-'+topping.title())
