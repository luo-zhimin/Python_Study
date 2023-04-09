"""
    python 操作mysql数据库
"""
from pymysql import Connection

conn = Connection(
    host='localhost',  # 主机名
    port=3306,  # 端口
    user='root',  # 用户
    password='2020.0.l',  # 密码
    autocommit=True  # 自动提交
)

# 获取服务端
# print(conn.get_server_info())

# 执行sql
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("student")
# 执行 非查询
# cursor.execute("create table test_pysql(id int)")
# 查询
# cursor.execute("select * from sys_dept")
# 获取查询结果 - tuple
# results: tuple = cursor.fetchall()
# for r in results:
#     print(r)
# print(results)

# 执行数据插入
cursor.execute("insert into sys_dept values (18,15,'软件C班',0,0)")
# 手动确认
# conn.commit()
# 关闭
conn.close()
