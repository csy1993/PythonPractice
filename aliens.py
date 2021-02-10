'''
* @Author: csy 
* @Date: 2019-04-28 13:47:42 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:47:42 
'''
# alien_0 = {'color': 'green', 'point': 5}
# alien_1 = {'color': 'yellow', 'point': 10}
# alien_2 = {'color': 'red', 'point': 15}
# aliens=[alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)
#
# aliens=[]
# for alien_number in range(30):
#     new_alien={'color': 'green', 'point': 5,'speed':'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:
#     print(alien)
# print('...')
# print('Total number of aliens:'+str(len(aliens)))
#
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:  # 取头3个
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'
for alien in aliens[-3:]:  # 取尾3个
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['point'] = 15
        alien['speed'] = 'fast'
for alien in aliens[:5]:
    print(alien)
print('...')
for alien in aliens[-5:]:
    print(alien)
