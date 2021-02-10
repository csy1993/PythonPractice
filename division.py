'''
* @Author: csy 
* @Date: 2019-04-28 14:58:29 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 14:58:29 
'''
# try:
#     print(5/0)
# except:
#     print("You can't divide by zero!")
print("Give me two numbers to deivide.\n(Enter 'q' to quit.)")
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0.")
    else:
        print(answer)
