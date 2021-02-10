# dirt={
#     "name":"csy",
#     "age":"17",
# }
# print(dirt.items())
# print(dirt.keys())
# print(dirt.values())
# import re
# str1="csy@163.com"

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']

# ]
# print(L[0][0])

# import openpyxl

# wb=openpyxl.load_workbook('test.xlsx')
# print(wb.sheetnames)
# for sheet in wb:
#     print(sheet.title)

# p=1
# print(p-1==0)

from MyQR import myqr
myqr.run(words='https://iamcsy.top/',picture='beautiful.gif',colorized=True,save_name='csy.gif') 