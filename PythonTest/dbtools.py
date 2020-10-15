import pymysql

def query(sql):
    """
        方法：python连接查询数据库
        参数：
            sql： "select * from t_user where id = 255"
        返回值：
            ((1, username, passsword, ..), (2, username2, passsword2, ..),)
    """
    # 步骤1. 连接并且打开对应的数据库
    db = pymysql.connect(host="118.24.105.78",user="root", password="1qaz!QAZ123***123", db="ljtestdb")
    # 步骤2：获取查询窗口：游标
    cur = db.cursor()
    # 步骤3：执行sql语句
    cur.execute(sql)
    # 步骤4：获取对应的结果
    res = cur.fetchall()
    # 步骤5：关闭数据
    db.close()
    
    return res


def commit(sql):
    """
        方法：python连接增删改数据库
        参数：
            sql： 
        返回值：
            ((1, username, passsword, ..), (2, username2, passsword2, ..),)
    """
    # 步骤1. 连接并且打开对应的数据库
    db = pymysql.connect(host="118.24.105.78",user="root", password="1qaz!QAZ123***123", db="ljtestdb")
    # 步骤2：获取查询窗口：游标
    cur = db.cursor()
    # 步骤3：执行sql语句
    cur.execute(sql)
    # 步骤4：获取对应的结果
    db.commit()
    # 步骤5：关闭数据
    db.close()
    


if __name__ == "__main__":  # 为了防止其他文件导入这个dbtools的时候执行测试代码
    # sql = 'select * from orders where id = 10086'
    # r = query(sql)
    # print(len(r))


    # # 问题1：如何找到结果中的某个值
    # # print(r[2][1])

    # # 问题2：如何判断结果是否为空？
    # if r == ():
    #     print("sql没有结果")

    # 问题3： [] r={}

    # sql = "delete from orders where product = 'iPhone12 Pro'"
    # commit(sql)

    sql2 = "select * from orders"
    r = query(sql2)
    print(r)