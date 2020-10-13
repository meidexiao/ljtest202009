
# if的嵌套
a = int(input("请输入数字:"))
if a > 18:
    if a < 25: # 18<a<25
        print("花一样的年龄")
    else:  # a>=25
        print("xxxx")
else:
    print("<=18")
    if a == 15:
        print("15")
    else:
        print("不是15")

