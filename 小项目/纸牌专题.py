"""
用面向函数的思想，返回一个扑克牌列表，里面有52项，每一项是一个元组,从列表中取出一张牌
例如：[(‘红心’，2), (‘草花’，2), …(‘黑桃’，‘A’)]
"""""
def playing_card(rank,suits):
    card_list = []
    for r in rank:
        for s in suits:
            card_list.append((r, s))
    return card_list
rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']  # 将rank作为行
suits = ['红心', '方块', '梅花', '黑桃']  # 将suits作为列
print(playing_card(rank,suits))
print(playing_card(rank,suits)[3])
"""
用面向对象的思想，返回一个扑克牌列表，里面有52项，每一项是一个元组,
并从中随机取出一张牌
"""
'''
纸牌游戏涉及的知识点：
1、collections模块的namedtuple
    #namdtuple(给元组起的名字，[元素名1，元素名2])
    #可命名元组的属性一旦创建就不再改变了，且可以使用属性名直接访问值
2、for循环的嵌套（结合行和列的for循环来理解）
3、列表推导式
4、random模块中的choice
    #choice依赖于内置函数__len__方法和__getitem__方法
5、random模块中的shuffle
    #shuffle依赖于内置函数__len__方法、__getitem__方法、__setitem__方法
'''
from random import choice
from random import shuffle
from collections import namedtuple
Card = namedtuple('Card',['rank','suits']) #相当于实例化一个对象Card，此步是定义列表的属性
class FranchDeck:
    rank = [str(n) for n in range(2,11)]+list('JQKA')
    suits = ['红心','方块','梅花','黑桃']
    def __init__(self):
        #将每一张牌（大小，花色）作为一个元素放到card这个列表中
        self.card = [Card(rank,suits) for rank in FranchDeck.rank for suits in FranchDeck.suits]
    def __len__(self):
        return len(self.card)
    def __getitem__(self, item):
        return self.card[item]
    def __setitem__(self, key, value):
        self.card[key] = value
f = FranchDeck()
print(f[0])#Card(rank='2', suits='红心')
#洗牌需要重置，所以用到__setitem__方法
shuffle(f)#相当于shuffle(f.card)
print(f[0])#Card(rank='4', suits='黑桃')
print(choice(f))
print(choice(f))







