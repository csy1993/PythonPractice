'''
* @Author: csy 
* @Date: 2019-04-28 15:22:25 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 15:22:25 
'''
filename = 'alice.txt'
try:
    with open(filename, 'rb')as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry,the file "+filename+" doesn't exist."
    print(msg)
else:
    print("The file "+filename+" has about " +
          str(len(contents.split()))+' words.')
