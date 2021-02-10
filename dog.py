'''
* @Author: csy 
* @Date: 2019-04-28 09:08:56 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 09:08:56 
'''
#!/usr/bin/python3
# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age < 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age -2)*5
#     print("对应人类年龄: ", human)
# input("点击 enter 键退出")


class Dog():
    '''一次模拟小狗的简单尝试'''

    def __init__(self, name, age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age

    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title()+' is now sittting.')

    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print(self.name.title()+' rolled over!')


my_dog = Dog('willie', 6)
print("My dog's name is "+my_dog.name.title())
print('My dog is '+str(my_dog.age)+' years old.')
my_dog.sit()
my_dog.roll_over()
