# 导入数据处理的模块
import json

from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='2020.0.l',
    autocommit=True
)

cursor = conn.cursor()
# 创建数据库 创建表
# cursor.execute("CREATE DATABASE py_sql")
conn.select_db("py_sql")
# table

# cursor.execute
# ("create table if not exists orders
# (order_date date,order_id varchar(255),money int,province varchar(10))")

# 组装mysql
# insert
# orders: list[data_define.Order] = objectExercise.all_orders
# print(orders)
# for order in orders:
#     sql = f"insert into orders(order_date,order_id,money,province) " \
#           f"values ('{order.date}','{order.order_id}',{order.money},'{order.province}')"
#     # print(sql)
#     # 执行sql
#     cursor.execute(sql)

# 查询 写出
cursor.execute("select * from orders")
orders: tuple = cursor.fetchall()
order_list = []
for order in orders:
    # 转换为列表 进行 写出
    # order[0].day
    day = None
    if len(str(order[0].day)) == 1:
        day = f'0{order[0].day}'
    else:
        day = order[0].day
    order_dict = {'date': f"{order[0].year}-0{order[0].month}-{day}", 'order_id': order[1], 'money': order[2],
                  'province': order[3]}
    # print(order_dict)
    # print(list(order))
    order_list.append(order_dict)
f = open('../sql/tempOrders.json', 'w', encoding='utf-8')
f.write(json.dumps(order_list))
f.close()
print(order_list)
conn.close()
