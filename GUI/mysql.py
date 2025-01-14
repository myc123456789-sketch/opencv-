import pymysql


def add(name, num):
    con = pymysql.connect(
        host='localhost',
        user='root',
        passwd='root',
        port=3306,
        charset='utf8',
        database='demo'
    )
    # 创建游标
    cur = con.cursor()
    # 定义SQL
    sql = 'insert into user (user_name,user_num) values (%s,%s)'
    # 运行sql(增删改查sql函数）
    cur.execute(sql, (name, num))
    # 执行增删改sql函数，返回一个受影响行数的数据
    num = cur.rowcount
    if num > 0:
        print('新增成功')
    else:
        print('新增失败')
    # 提交
    con.commit()
    # 释放资源
    cur.close()
    con.close()


def update(name, id):
    con = pymysql.connect(
        host='localhost',
        user='root',
        passwd='root',
        port=3306,
        charset='utf8',
        database='demo'
    )
    # 创建游标
    cur = con.cursor()
    # 定义SQL
    sql = 'UPDATE user set user_name=%s where user_num=%s'
    # 运行sql(增删改查sql函数）
    cur.execute(sql, (name, id))
    # 执行增删改sql函数，返回一个受影响行数的数据
    num = cur.rowcount
    if num > 0:
        print('更新成功')
    else:
        print('更新失败')
    # 提交
    con.commit()
    # 释放资源
    cur.close()
    con.close()


def query(num):
    con = pymysql.connect(
        host='localhost',
        user='root',
        passwd='root',
        port=3306,
        charset='utf8',
        database='demo'
    )
    # 创建游标
    cur = con.cursor()
    # 定义SQL
    sql = "select * from user where user_num=%s"
    # 运行sql（增删改查sql的函数）
    cur.execute(sql, (num,))
    # 查询
    rs = cur.fetchall()
    print(rs)
    print(rs[0][1])
    cur.close()
    con.close()
    if len(rs) > 0:
        return rs[0][1]
    else:
        return "查无此人"


def delete(id):
    #创建数据库连接
    con = pymysql.connect(
        host="localhost",#数据库地址
        user="root",#用户名
        passwd="root",#密码
        port=3306,#端口
        database="demo",#数据库名
        charset="utf8" #中文编码
    )
    #创建游标对象,包含了增删改查的函数
    cur = con.cursor()
    #定义sql
    sql = "delete from user where user_id=%s"
    #运行sql（增删改查sql的函数）
    cur.execute(sql, (id,))
    #执行增删改sql的函数,返回一个受影响行数的数值
    num = cur.rowcount
    if num > 0:
        print("删除成功")
    else:
        print("删除失败")
    #提交
    con.commit()
    #释放资源
    cur.close()
    con.close()


if __name__ == '__main__':
    add('王五', 1)
    update('张三', 1)
    query(1)
    delete(1)
