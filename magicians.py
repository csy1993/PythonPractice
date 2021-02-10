'''
* @Author: csy 
* @Date: 2019-04-28 13:55:24 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:55:24 
'''
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title()+",that was a great trick!")
    print("I can't wait to see your next trick," + magician.title()+".\n")
print("Thank you,everyone.That was a great magic show.\n")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)  # 缩进错误
