account = {"username":"liuyun", "password":"a12345678"}
username = input("请输入账号:")
password = input("请输入密码:")

# 拿输入的账号密码和对应的字典里面的值判断
if username == account["username"] and password == account["password"]:
    print("账号登录成功")
else:
    print("账号登录失败")



# 添加用户密码练习：
# 有一个字典account = {"username":"test"}
# 如果输入用户名为test，那在account中增加一个键值对，password 
# 输出的内容 account = {"username":"test", "password":"12345678"}
# 如果用户名不是test，那就显示账号不对
account = {"username":"test"}
username = input("请输入账号:")
if account.get("username") == username:
    account["password"] = "12345678"
    print(account)
else:
    print("账号不对")
