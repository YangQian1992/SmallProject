'''
抢红包所用的知识点：
1、random.sample(数字范围，选择的数字个数)--->返回的是一个列表
2、list.extend()---->迭代着添加到字典中
3、sorted(list)--->对序列进行从小到大排序
4、列表推导式---->[i*2 for i in [1,2,3,4]](遍历模式)
5、了解数据结构的算法思想
'''
# #基础版
# import random
# money = 20
# person = 10
# num_list = random.sample(range(1,20*100),person-1)
# print(num_list)#[465, 1234, 426, 951, 131, 91, 1931, 1742, 1612]
# num_list.extend([0,20*100])
# print(num_list)#[465, 1234, 426, 951, 131, 91, 1931, 1742, 1612, 0, 2000]
# res_list = sorted(num_list)
# print(res_list)#[0, 91, 131, 426, 465, 951, 1234, 1612, 1742, 1931, 2000]
# list = []
# for index in range(person):
#     num = (res_list[index+1] - res_list[index])/100
#     list.append(num)
# print(list)#[0.91, 0.4, 2.95, 0.39, 4.86, 2.83, 3.78, 1.3, 1.89, 0.69]
#
# #函数版
# import random
# def red_packet(money,num):
#     ret = random.sample(range(1,20*100),num-1)
#     ret.extend([0,20*100])
#     ret = sorted(ret)
#     list = []
#     for index in range(num):
#         i = (ret[index+1] - ret[index])/100
#         list.append(i)
#     return list
# print(red_packet(20,6))
#
# #升级版
# import random
# def red_packet(money,num):
#     ret = random.sample(range(1,money*100),num-1)
#     ret.extend([0,money*100])
#     ret.sort()
#     return [(ret[index+1]-ret[index])/100 for index in range(num)]
# print(red_packet(20,6))#[8.6, 7.48, 0.23, 2.21, 1.23, 0.25]
#
# #生成器函数
# import random
# def red_packet(money,num):
#     ret = random.sample(range(1,money*100),num-1)
#     ret.extend([0,money*100])
#     ret.sort()
#     for index in range(num):
#         yield (ret[index+1]-ret[index])/100
# obj = red_packet(20,6)




