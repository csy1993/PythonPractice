'''
* @Author: csy 
* @Date: 2019-04-28 13:55:50 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:55:50 
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'  # 输出第1个元素
print(motorcycles)
motorcycles[0] = 'honda'

motorcycles.append('ducati')  # 在末尾添加元素
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
print(motorcycles)
motorcycles.append('yamaha')
print(motorcycles)
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')  # 将元素插入第1位
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]  # 删除第1个元素
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()  # 取走最后1个元素
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a "+last_owned.title()+".")

first_owned = motorcycles.pop(0)  # 取走第1个元素
print("The first motorcycle I owned was a "+first_owned.title()+".")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")
