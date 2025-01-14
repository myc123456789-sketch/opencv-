import pymysql


def link():
    con = pymysql.connect(
        host='localhost',
        user='root',
        passwd='root',
        port=3306,
        charset='utf8',
        database='demo'
    )
    cur = con.cursor()
    return cur, con


def add(name, path):
    cur, con = link()

    # 定义SQL
    sql = 'insert into people (people_name,people_path) values (%s,%s)'
    # 运行sql(增删改查sql函数）
    cur.execute(sql, (name, path))
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


def query(id):
    cur, con = link()
    # 定义SQL
    sql = "select people_name from people where people_id=%s"
    # 运行sql（增删改查sql的函数）
    cur.execute(sql, (id,))
    # 查询
    rs = cur.fetchall()

    cur.close()
    con.close()
    if len(rs) > 0:
        pass
    else:
        return "查无此人"
    return rs



