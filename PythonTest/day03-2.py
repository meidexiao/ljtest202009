import time

# while
# a = 1
# b = 2

# # 死循环
# while b > a:
#     print("是滴")
#     a = a + 1


# 红绿灯
# 使用python打印红绿灯，红灯打印30次，绿灯打印25次，黄灯5次
while True:
    for i in range(60): # 0-29:print红灯； 30-54：绿灯； 55-59：黄灯
        if i < 30:
            print("红灯")
        if i > 29 and i < 55:
            print("绿灯")
        if i > 54:
            print("黄灯")
        time.sleep(1)  # 代码等待1s
