from dbtools import query

username = input("请输入账号：")
password = input("请输入密码：")

sql = "select * from t_pymysql_account where username='{}' and password='{}'".format(username, password)
print(sql)
r = query(sql)
if len(r) != 0:
    print("登录成功")
else:
    print("登录失败")