# a = 1
# b = "1"
# print(type(b))
# # 1.数字转字符串
# c = str(123)
# print(type(c))

# # 2.字符串转数字
# d = int(b)
# print(d)

# e = "aa"
# int(e)

# 元组和数组
cc = (1,2,3,4)
dd = list(cc)
print(dd)
ee = tuple(dd)
print(ee)

# 字符串>字典, eval
q = "{'username':'乔妹二'}"
o = "(1,2,3)"
print(type(eval(o)))# 把对应的字符串格式转换成对应的类型
print(type(eval(q)))
