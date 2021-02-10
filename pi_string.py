'''
* @Author: csy 
* @Date: 2019-04-28 14:41:49 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 14:41:49 
'''
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:100])
print(len(pi_string))
birthday = input('Enter your birthday(yyyymmdd):')
if birthday in pi_string:
    print('Your birthday appears.')
else:
    print('Your birthday does not appear.')
