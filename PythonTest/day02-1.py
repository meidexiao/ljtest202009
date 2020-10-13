a = {"xm":"游世杰", "yz":"高", "删库":"YES","age":123, "gf":["凤姐", "芙蓉姐姐", "巧碧螺"]}
# key-value， key不能重复

print(len(a))

#取值:a[""]如果去取不存在的key，会报错；get方法默认是None
b = a["xm"]
c = a.get("yz")
print(b)
print(c)

# 增加
a["sg"] = 190
print(a)

# 修改：此时是修改
a["sg"] = 180
print(a)

# 删除：删除某个键值对
del a["sg"]
print(a)

# 全部删除
a.clear()
print(a)


