import requests
from dbtools import query
from filetools import read_file
from filetools import write_file

# 使用get方法去请求这个接口
# res = requests.get("http://118.24.105.78:2333/get_title_img")
# # 打印返回值信息
# print(res.text)

u = "http://118.24.105.78:2333/login"               # 接口地址
h = {"Content-Type":"application/json"}             # 请求头
d = {"username":"liuyun1", "password":"a12345678"}  # 请求参数
r = requests.post(url=u, headers=h, json=d)
# print(r.text)                                      # r.text：响应值
# assert 条件语句
# 2.判断结果
assert r.status_code == 200         # 判断状态码
assert r.json()["status"] == 200    # 判断结果码

# 3.数据库查询
sql = "select * from t_user where username='{}'".format(d["username"])
assert len(query(sql)) != 0          # 如果账号存在 > sql应该是有结果的 > query(sql)长度 != 0
print("登录接口测试用例执行通过！")


# 保存token到user_token.txt文件中
token = r.json()["data"]["token"]
write_file("./user_token.txt", token)

# 用户退出
nt = read_file("./user_token.txt")
u = "http://118.24.105.78:2333/logout"               # 接口地址
h = {"Content-Type":"application/json","token":nt}             # 请求头\
r = requests.get(url=u, headers=h)
print(r.text)