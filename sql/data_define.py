# 读取数据封装
class Order:
    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self) -> str:
        return f"Order类[date:{self.date},order_id:{self.order_id},money:{self.money},province:{self.province}]"
