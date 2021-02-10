'''
* @Author: csy 
* @Date: 2019-04-28 13:43:52 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:43:52 
'''
# favorite_languages={
# 	'jen':'python',
# 	'sarah':'c',
# 	'edward':'ruby',
# 	'phil':'python',
# }
#
# print("Sarah's favorite language is "+favorite_languages['sarah'].title())
#
# for name,language in favorite_languages.items():	#提取字典
# 	print(name.title()+"'s favorite language is "+language.title())
#
# for name in favorite_languages.keys():	#提取关键字
# 	print(name.title())
#
# friends=['phil','sarah']
# for name in favorite_languages.keys():
# 	print(name.title())
# 	if name in friends:
# 		print('Hi,' + name.title() +',your favorite language is '+favorite_languages[name].title())	#根据关键字提取指
#
# for name in sorted(favorite_languages.keys()):	#对关键字进行排序
# 	print(name.title()+',thank you for taking the poll.')
#
# print('The following languages have been mentioned')
# for language in favorite_languages.values():	#提取值
# 	print(language.title())
#
# print('The following languages have been mentioned')
# for language in set(favorite_languages.values()):	#去除重复项
# 	print(language.title())
#
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(name.title()+"'s favorite languages are:")
    for language in languages:
        print('\t'+language)
    print()
