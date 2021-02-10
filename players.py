'''
* @Author: csy 
* @Date: 2019-04-28 13:57:06 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:57:06 
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
