# 循环》遍历

# 字符串
# username = "刘飞儿游世杰贼厉害"
# j = 1
# for i in username:
#     print("这是第{}次运行 》 i的值是【{}】".format(j, i))
#     j = j + 1 # 自增 j = 1 + 1  》 j = 2

# 遍历元组
# username = ("游","世","杰","贼","厉","害", "能","删","库","会","跑","路")
# for i in username:
#     print(i)

# 遍历数组
# username = ["游","世","杰","贼","厉","害", "能","删","库","会","跑","路"]
# for i in username:
#     print(i)

# 使用for循环去取出1这个数字
# username = ["游","世", [1,3,4]]
# for i in username:
#     # 如何去判断i是最后一个元素
#     if type(i) == list:
#         print(i)


# 使用for循环去取出字典的值
# account = {"username":"游世杰", "jn":"sql"}
# for i in account:
#     # account[i] # i = "username" > account["username"]
#     print(account[i])


# 注册一个用户
# 如果用户已经存在，那么打印注册使用，用户已存在，
# 如果用户不存在，那么去添加一个用户信息
# 栗子：用户名：陈梦阳， a123456》成功；刘军》注册失败 


# 看不懂不要紧，能理解就更好。
# account = [
#         {"username":"游世杰", "password":"a12345678"}, 
#         {"username":"刘军", "password":"a12345678"}
#     ]
# # len(account) # 最后一次循环和account有什么关系?
# u = input("请输入用户名:")
# j = 1 # 运行的次数 j > 2 刘军 > 最后一次 > len(account)
# for i in account:
#     if i["username"] == u:
#         print("用户名已存在，注册失败")
#         break
#     else:
#         # 判断是否为最后一个账号
#         if j == len(account):
#             print("用户名不存在，开始注册")
#             new_user = {"username":u, "password":"a12345678"}
#             account.append(new_user)
#             # 终止循环
#             break
#     print("==========================================")
#     j = j + 1
    
# print(account)


# a = [1,2,3]
# for i in a:
#     if i == 2:
#         continue # 直接跳转到下一个循环
#     print(i)
# 打印10以内的奇数
# a = [1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(1,11): # range(10) = (0,1,2,3,4,5,6,7,8,9) # range(1, 10):从1开始，生成9个数字
#     print(i)