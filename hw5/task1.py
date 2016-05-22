import sqlite3 as sq

with sq.connect('/Users/Leria/Downloads/data.sqlite') as data:
    cur = data.cursor() #create cursor for making queries

    # for row in cur.execute('select * from GoodsInOrders limit 2'):
    #     print(row)

    for row in cur.execute('select * from Users'):
        print(row)

    for row in cur.execute('select count(*) from Users'):
        print(row)

    for row in cur.execute('select count(*) from Users where birth_date >= date("1976-05-13")'):
        print(row)

    for row in cur.execute('select count(*), country from Users group by country'):
        print(row)

    for row in cur.execute('select name, count(*) as num from users group by name having num > 1'):
        print(row)

    for row in cur.execute('select count(*) from Orders where created >= date("2016-01-01") and created < date("2017-01-01")'):
        print(row)

    for row in cur.execute('select id, name, count(*) as num from GoodsInOrders '
                           'inner join Goods on id = good_id '
                           'group by good_id '
                           'order by num desc limit 10'):
        print(row)

    for row in cur.execute('select sum(paid) / count(*) from Orders'): #!!!!!!!!!!!!
        print(row)

    for row in cur.execute('select * from Goods where name like "%bread%"'):
        print(row)

    for row in cur.execute('select id, name, count(*) as num from GoodsInOrders '
                           'inner join Goods on id = good_id '
                           'group by good_id '
                           'order by num desc limit 10;'):
        print(row)

    for row in cur.execute('select sum(price) from Goods '
                           'inner join Orders on Orders.id = order_id '
                           'inner join GoodsInOrders on Goods.id = good_id '
                           'where paid = 1;'):
        print(row)

    for row in cur.execute('select Goods.id, Goods.name from Goods '
                           'inner join Orders on order_id = Orders.id '
                           'inner join GoodsInOrders on Goods.id = good_id '
                           'inner join Users on Users.id = user_id '
                           'where gender = "F" '
                           'group by Goods.name '
                           'order by count(*) desc '
                           'limit 10;'):
        print(row)

    for row in cur.execute('select Users.id, Users.name from Users '
                           'inner join Orders on Users.id = user_id '
                           'inner join GoodsInOrders on Orders.id = order_id '
                           'inner join Goods on Goods.id = good_id '
                           'where units = "KG" '
                           'group by user_id '
                           'order by sum(quantity) desc '
                           'limit 1;'):
        print(row)

###################

unpaid_query = "select Users.name, Orders.id, sum(price) from Users " \
               "inner join Orders on Users.id = user_id " \
               "inner join GoodsInOrders on Orders.id = order_id " \
               "inner join Goods on Goods.id = good_id " \
               "where paid = 0 and Users.id = ? " \
               "group by Orders.id"

def unpaid(user_id):
    with sq.connect("data.sqlite") as data:
        cur = data.cursor()
        unpaid_items = cur.execute(query, [user_id]).fetchall()
    return unpaid_items