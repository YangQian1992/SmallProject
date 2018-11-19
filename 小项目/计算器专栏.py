import re

"""
模拟计算器:实现能计算1 - 2 * ( (60-30 + (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) * (-40/5) - (-4*3)/ (16-3*2) )等类似公式的计算器程序
"""
# 匹配乘除---》数字/数字   或者   数字*数字
# multiplier_obj = re.search("\d+(\.\d+)?[*/]-?\d+(\.\d+)?",bracket_content)
# if multiplier_obj:pass
# multiplier_content = multiplier_obj.group()#"2*5"
# 自定义计算乘除的函数
def calculate_the_multiplier(expression):  # expression = multiplier_content = "2*5"
    # 判断除号是否在此字符串中
    if '/' in expression:
        a, b = expression.split("/")
        return str(float(a) / float(b))
    elif '*' in expression:
        a, b = expression.split("*")
        return str(float(a) * float(b))
# 将计算乘除的方法的返回值赋值给multiplication_division_return_value变量
# multiplication_division_return_value = calculate_the_multiplier(multiplier_content)#"10.0"
# 将括号中的乘除运算替换成计算完的返回值
# minus_multiplication_division = bracket_content.replace(multiplier_content,multiplication_division_return_value)#"(10.0)"
# 此时问题是：括号内若有多个乘除运算呢，不只是一个乘除运算的场景该怎么办？
def minus_multiplication_division(exp):  # exp = bracket_content = "(9-2*5/3+7/3*99/4*2998+10*568/14)"
    while True:
        # 匹配乘除---》数字/数字   或者   数字*数字
        multiplier_obj = re.search("\d+(\.\d+)?[*/]-?\d+(\.\d+)?", exp)
        if multiplier_obj:
            multiplier_content = multiplier_obj.group()  # "2*5"
            # 调用计算乘除的函数，并将此函数的返回值赋值给multiplication_division_return_value变量
            multiplication_division_return_value = calculate_the_multiplier(multiplier_content)  # "10.0"
            # 将括号中的乘除运算替换成计算完的返回值
            exp = exp.replace(multiplier_content, multiplication_division_return_value)
        else:
            break
    return exp


# 自定义计算加减的函数
def calculation_subtract(expression):
    # 匹配加减---》数字+数字   或者   数字-数字
    add_subtract_obj = re.finditer('-?\d+(\.?\d+)?', expression)
    sum = 0
    for item in add_subtract_obj:
        sum += float(item.group())
    return str(sum)  # '173545.88095238098'

#自定义格式化函数
def exp_format(exp):
    exp = exp.replace("++", "+")
    exp = exp.replace("+-", "-")
    exp = exp.replace("-+", "-")
    exp = exp.replace("--", "+")
    return exp

#自定义去除括号函数
def remove_parenthesis(s):
    while True:
        # 先匹配括号
        bracket_obj = re.search("\([^()]+\)", s)
        # 判断存在匹配结果
        if bracket_obj:
            bracket_content = bracket_obj.group()  # "(9-2*5/3+7/3*99/4*2998+10*568/14)"
            ret_minus_mud = minus_multiplication_division(bracket_content)
            # 计算完乘除替换掉后需要格式化一下
            ret_minus_mud = exp_format(ret_minus_mud)  # (9-3.3333333333333335+173134.50000000003+405.7142857142857)
            ret_remove_parenthesis = calculation_subtract(ret_minus_mud)  # '173545.88095238098'
            # 计算完加减后需要将s中的括号替换
            s = s.replace(bracket_content, ret_remove_parenthesis)
            # 替换后需要格式化一下
            s = exp_format(s)
        else:
            break
    # 计算乘除法并将返回值返回给remove_chengchu
    remove_chengchu = minus_multiplication_division(s)  # 1--2777211.6952380957
    # 计算乘除后格式化一下
    remove_chengchu = exp_format(remove_chengchu)  # 1+2777211.6952380957
    # 计算加减法并将返回值给res
    res = calculation_subtract(remove_chengchu)  # 2777212.6952380957
    # 将res返回给调用者
    return res


s = "1 - 2 * ( (60-30 + (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) * (-40/5) - (-4*3)/ (16-3*2) )"
# 去字符串中的空格
s = s.replace(" ", "")
print(f'最终计算的结果是：{remove_parenthesis(s)}', f'此结果的数据类型是：{type(remove_parenthesis(s))}')
