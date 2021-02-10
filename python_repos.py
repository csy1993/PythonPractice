'''
* @Author: csy 
* @Date: 2019-06-19 20:54:54 
* @Last Modified by:   csy 
* @Last Modified time: 2019-06-19 20:54:54 
'''
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import webbrowser

url='https://api.github.com/search/repositories?q=language:python&sourt=stars'
r=requests.get(url)
# print("Status code:",r.status_code)
response_dict=r.json()
# print(response_dict.keys())
# print("Total repositories:",response_dict['total_count'])

repo_dicts=response_dict['items']
# print("Repositories returned:",len(repo_dicts))

repo_dict=repo_dicts[0]
# print("\nKeys:",len(repo_dict))

# for key in sorted(repo_dict.keys()):
#     print(key)
# for repo_dict in repo_dicts:
#     print("\nName:",repo_dict['name'])
#     print("\nOwner:",repo_dict['owner']['login'])
#     print("\nStars:",repo_dict['stargazers_count'])
#     print("\nRepository:",repo_dict['html_url'])
#     print("\nDescription:",repo_dict['description']+'\n\n\n')

names,stars,plot_dicts=[],[],[]

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    plot_dict={
        'value':repo_dict['stargazers_count'],
        'label':repo_dict['description'],
        'xlink':repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)
my_style=LS('#333366',base_style=LCS)

my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=18
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000

chart=pygal.Bar(my_config,style=my_style)
chart.title='Most-Starred Python Projects on Github'
chart.x_labels=names
chart.add('',stars)
chart.render_to_file('python_repos.svg')
webbrowser.open('python_repos.svg') 


chart2=pygal.Bar(my_config,style=my_style)
chart2.title='Most-Starred Python Projects on Github   2'
chart2.x_labels=names
chart2.add('',plot_dicts)
chart2.render_to_file('python_repos2.svg')
webbrowser.open('python_repos2.svg') 