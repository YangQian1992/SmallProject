""""
写两个文件，将两个文件作为参数，判断这两个文件是否相同，如果相同，返回True,否则返回False.
"""
# 比较两个文件内容是否相同
#     涉及到的知识点：1、os模块--->得到文件大小os.path.getsize(绝对路径/相对路径)
#                     2、hashlib模块--->三步走：创建md5对象                md5_obj = hashlib.md5()
#                                               获取摘要（bytes型）        md5_obj.update(字符串.encode('utf-8'))
#                                               将摘要转换成字符串形式     md5_obj.hexdigest()
#                     3、数据很大时，需要分段按字节截取摘要，注意需要创建两个md5对象：md5_f1_content 和 md5_f2_content
import hashlib
import os
def match_the_file(path1,path2):
    with open(path1, encoding='utf-8')as f1:
        f1_size = os.path.getsize(path1)
        md5_f1_content = hashlib.md5()  # 注意：1、创建一个对象md5_f1_content 2、作用域---放在while循环外
        while f1_size > 0:
            f1_content = f1.read(1024)
            md5_f1_content.update(f1_content.encode('utf-8'))
            f1_size -= 1024
        str_f1_content = md5_f1_content.hexdigest()
    with open(path2, encoding='utf-8')as f2:
        f2_size = os.path.getsize(path2)
        md5_f2_content = hashlib.md5()# 注意：1、创建一个对象md5_f2_content 2、作用域---放在while循环外
        while f2_size > 0:
            f2_content = f2.read(1024)
            md5_f2_content.update(f2_content.encode('utf-8'))
            f2_size -= 1024
        str_f2_content = md5_f2_content.hexdigest()
    if str_f1_content == str_f2_content :return True
    else:return False
print(match_the_file('F:\python全栈开发12期_pycharm\Day24\京东','F:\python全栈开发12期_pycharm\Day25\京东'))#True