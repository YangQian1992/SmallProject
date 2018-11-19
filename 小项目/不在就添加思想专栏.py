#不在就添加的编程思想：
#   创建一个空的数据类型(空字符串/空列表/空字典)
#   遍历已有的可迭代对象的所有元素
#       判断元素是否在创建的空数据类型中
#           如果不在就将此元素添加进去或者对此元素操作一番
"""
例1：编写程序，统计如下各个字符串个数。
如，有此字符串str1 = "hello world god is allways busy"，
最后得到的结果为：‘h:1,e:1,l:5,o:3,w:2,r:1,d:2,g:1,i:1,s:3,a:2,y:2,b:1,u:1,’
"""
s = "hello world god is allways busy"
s = s.replace(" ","")
# 创建一个空字符串
res = ""
# 遍历整个可迭代对象
for item in s:
    #判断元素是否在新创建的字符串中
    if item not in res:
        #若不在就进行根据需求对元素进行一番操作后添加到新字符串中；若在就进入下一次循环
        res = res + item + ":" + str(s.count(item)) + ","
print(res)

"""
例2：有如下值li= [11,22,33,44,55,77,88,99,90]，
将所有大于 66 的值保存至字典的第一个key中，
将小于 66 的值保存至第二个key的值中。
"""
li= [11,22,33,44,55,77,88,99,90]
#创建一个空字典
new_dict = {}
#遍历整个可迭代对象
for item in li:
    if item < 66 :
        # 判断“k1”是否在创建的空字典键中
        if "k1" not in new_dict.keys():
            #若不在就添加键，默认值为空列表；
            new_dict["k1"] = []
        #若在就直接将元素添加到此字典中，进行下一次循环
        new_dict["k1"].append(item)
    elif item > 66 :
        # 判断“k2”是否在创建的空字典键中
        if "k2" not in new_dict.keys():
            # 若不在就添加键，默认值为空列表；
            new_dict["k2"] = []
        # 若在就直接将元素添加到此字典中，进行下一次循环
        new_dict["k2"].append(item)
print(new_dict)
"""
例3：按要求完成下列转化
如何把上list1转换成下方的列表？
list2 = [
    {"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]},
    {"name": "wusir", "hobby_list": ["喊麦", "街舞"]},
]
"""
list1 = [
    {"name": "alex", "hobby": "抽烟"},
    {"name": "alex", "hobby": "喝酒"},
    {"name": "alex", "hobby": "烫头"},
    {"name": "alex", "hobby": "Massage"},
    {"name": "wusir", "hobby": "喊麦"},
    {"name": "wusir", "hobby": "街舞"},
]
#转换思想：dict---> {"alex":{"name":"alex","hobby_list":["抽烟", "喝酒", "烫头", "Massage"]},"wusir":{"name":"wusir","hobby_list":["喊麦", "街舞"]}}
#          list2 = list(dict.values())


#创建一个空字典
person_dict = {}
for item in list1:
    #判断“name”所对应的值是否在新建字典的键中，若不在就先添加键和值
    if item["name"] not in person_dict:
        person_dict[item["name"]] = {"name":item["name"],"hobby_list":[item["hobby"],]}
    else:
        #若在就直接添加"hobby_list"所对应的值
        person_dict[item["name"]]["hobby_list"].append(item["hobby"],)
print(list(person_dict.values()))
"""
例4：模拟公司HR将员工信息录入公司内部系统。
录入的员工信息表的数据类型如下：
1，HR选择添加员工信息或者退出。
2，分别将员工的姓名，年龄，性别，婚否，学历这几项依次录入员工信息表中，
其中id为自增（id不用HR填写，而是每添加一个员工信息就自动加1，并且id是唯一的）。
3，如果遇到录入员工信息时有相同的姓名，那么就将相同的姓名的员工的
名字变成  名字+id（如之前录入了一个名叫张三的员工，之后新员工又有同名的情况也叫张三，
那么后面这个张三名字要改成 张三2（此id为他的对应的id））。
4，退出整个程序时，最后要将本次录入的所有的员工姓名依次打印出来。
"""
user_list = [
    {'id':1,
     'personal_info':
         {'name':'老男孩',
          'age':56,
          'sex':'男',
          'marry_status':'是',
          'edu_background':'本科'}
     }
]
#转换思想：{"老男孩":{'name':'老男孩','age':56 ,'sex':'男', 'marry_status':'是', 'edu_background':'本科'}}
try:
    person_dict = {}
    id = 1
    while True:
        content = input("请输入员工姓名，年龄，性别，婚否，学历(Q/q退出):").strip()
        if content.upper() == "Q":
            for item in user_list[1:]:
                print(item['personal_info']["name"])
            break
        else:
            name,age,sex,marry_status,edu_background = content.replace("，",",").split(",")
            #判断姓名是否在字典键中，若不在就先添加此姓名的键值对
            if name not in person_dict:
                person_dict[name] = {"name":name,"age":int(age),"sex":sex,"marry_status":marry_status,"edu_background":edu_background}
            else:
                #若在(即姓名相同)就将相同的姓名的员工的名字变成  名字+所对应的id
                person_dict[name] = {"name": name + str(id+1), "age": int(age), "sex": sex, "marry_status": marry_status,"edu_background": edu_background}
            user_list.append({'id': id + 1, 'personal_info': person_dict[name]})
            id += 1
except ValueError:
    print("输入内容不符要求")
