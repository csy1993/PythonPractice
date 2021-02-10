'''
* @Author: csy 
* @Date: 2019-04-28 16:44:53 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 16:44:53 
'''
from name_function import get_formatted_name
print("Enetr 'q' to quit.")
while True:
    first = input("\nFirst name:")
    if first == 'q':
        break
    last = input("Last name:")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\nName:"+formatted_name)
