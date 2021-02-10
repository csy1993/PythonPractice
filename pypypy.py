'''
* @Author: csy 
* @Date: 2019-04-28 13:57:20 
* @Last Modified by:   csy 
* @Last Modified time: 2019-04-28 13:57:20 
'''
# print('每个铭文的攻击力是：' + str((362-330)/10))
#
# pay = 80
# if pay <= 500:
#     print("欢迎进入史塔克穷人帮前三名")
#     if pay > 100:
#         print("请找弗瑞队长加薪")
#     elif pay <= 100:
#         print('恭喜您荣获"美元队长"称号！')
# elif 500 < pay <= 1000:
#     print("祝贺您至少可以温饱了。")
# elif pay > 1000:
#     print("经济危机都难不倒您！")
#     if 1000 < pay <= 20000:
#         print("您快比钢铁侠有钱了！")
#     elif pay > 20000:
#         print("您是不是来自于瓦坎达国？")
# print("程序结束")
#
need = input('小精灵：您好，欢迎古灵阁，请问您需要帮助吗？需要or不需要？')
if need == '需要':
    server = int(input('小精灵：请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询'))
    if server == 1:
        print('请去存取款窗口')
    elif server == 2:
        print('金加隆和人民币的兑换率为1:51.3，即1金加隆=51.3人民币')
        sum = int(input('请问您需要兑换多少金加隆呢？'))
        print('那么，您需要付给我'+str(51.3*sum)+'人民币')
    elif server == 3:
        print('请去咨询窗口')
else:
    print('好的，再见.')
