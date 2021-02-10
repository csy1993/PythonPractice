'''
* @Author: csy 
* @Date: 2019-06-05 21:59:43 
* @Last Modified by:   csy 
* @Last Modified time: 2019-06-05 21:59:43 
'''
from die import Die
import pygal
import webbrowser

die1 = Die()
die2 = Die(10)
results = []
for roll_num in range(50000):
    result = die1.roll()+die2.roll()
    results.append(result)
frequencies = []
max_result = die1.num_sides+die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print("1 appear:"+str(frequencies[0]))
print("2 appear:"+str(frequencies[1]))
print("3 appear:"+str(frequencies[2]))
print("4 appear:"+str(frequencies[3]))
print("5 appear:"+str(frequencies[4]))
print("6 appear:"+str(frequencies[5]))
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Results"
hist.y_title = "Frequency of Result"
hist.add('D6+D10', frequencies)
hist.render_to_file('die_visual.svg')
webbrowser.open("die_visual.svg")