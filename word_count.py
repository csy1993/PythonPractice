'''
* @Author: csy 
* @Date: 2019-04-28 15:56:27 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 15:56:27 
'''


def count_words(filename):
    '''计算一个文件大致包含多少个单词'''
    try:
        with open(filename, 'rb')as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "Sorry,the file "+filename+" doesn't exist."
        # print(msg)
        pass
    else:
        print("The file "+filename+" has about " +
              str(len(contents.split()))+' words.')


filenames = ['alice.txt', 'foo.txt', 'foo1.txt', 'foo2.txt', 'foo3.txt']
for filename in filenames:
    count_words(filename)
