import mysql.connector
from flask import Flask, request,jsonify,render_template
import json

app = Flask(__name__,static_url_path='/static', static_folder='D:/database/static',template_folder = 'D:/database/templates')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/admin.html')
def admin():
    return render_template('admin.html')

@app.route('/try_admin.html')
def try_admin():
    return render_template('try_admin.html')

@app.route('/login.html')
def relogin():
    return render_template('login.html')

@app.route('/loginto.html')
def loginto():
    return render_template('loginto.html')

@app.route('/try_register.html')
def try_regiter():
    return render_template('try_register.html')

@app.route('/search.html')
def search():
    return render_template('search.html')


#处理favicon问题
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

#登录检查功能
@app.route('/login', methods=['POST'])
def login_check():
    # 连接 MySQL 数据
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()

    #读取用户信息
    Uname = request.get_json()['Uname']
    Upin = request.get_json()['Upin']
    
    #检测用户是否存在
    sql = "SELECT * FROM USERS WHERE Uname = %s"
    cursor.execute(sql,(Uname,))
    user_result = cursor.fetchall()
    if not user_result:
        return jsonify({'error':'用户名错误'})
    
    #检测密码是否正确
    sql = "SELECT Upin FROM USERS WHERE Uname = %s"
    cursor.execute(sql,(Uname,))
    user_result = cursor.fetchone()
    if(user_result[0] != Upin):
        return jsonify({'error':'密码错误'})
    success = {'success':True}
    cursor.close()
    mydb.close()
    return jsonify(success)

#管理员登录检查
@app.route('/try_admin', methods=['POST'])
def admin_check():
    # 连接 MySQL 数据
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()

    #读取用户信息
    Uname = request.get_json()['Aname']
    Upin = request.get_json()['Apin']
    
    #检测用户是否存在
    sql = "SELECT * FROM ADMIN WHERE Aname = %s"
    cursor.execute(sql,(Uname,))
    user_result = cursor.fetchall()
    if not user_result:
        return jsonify({'error':'用户名错误'})
    
    #检测密码是否正确
    sql = "SELECT Apin FROM ADMIN WHERE Aname = %s"
    cursor.execute(sql,(Uname,))
    user_result = cursor.fetchone()
    if(user_result[0] != Upin):
        return jsonify({'error':'密码错误'})
    success = {'success':True}
    cursor.close()
    mydb.close()
    return jsonify(success)


#推荐功能
@app.route('/recommoned', methods=['POST'])
def recommon():
    # 连接 MySQL 数据
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()
    #读取用户信息
    Uname = request.get_json()['Uname']
    print(Uname)
    #读取用户最大购买类别
    sql = "SELECT Gtype FROM GOODS WHERE Gname IN ( SELECT Gname FROM BUYINGS WHERE Uname = %s );"
    cursor.execute(sql,(Uname,))
    Utype = cursor.fetchall()
    utype = [item[0] for item in Utype]
    from collections import Counter
    count = Counter(Utype)
    utype = str(max(count, key=count.get)[0])
    sql = "SELECT Gno,Gname,Gprice FROM GOODS WHERE Gtype = %s"
    cursor.execute(sql, (utype,))
    Ubuy = cursor.fetchmany(3)
    fields = ['Gno','Gname','Gprice']
    ubuy_dict = [dict(zip(fields, row)) for row in Ubuy]
    print(ubuy_dict)



    while Ubuy:
        # 处理每个结果
        for result in Ubuy:
            # 处理结果的逻辑
            print(result)
        # 继续获取下一批结果
        Ubuy= cursor.fetchmany(3)




    # 构造响应对象
    response = {
        'success': True,
        'like': ubuy_dict
    }
    cursor.close()
    mydb.close()
    return jsonify(response)

    

#注册功能
@app.route('/register', methods=['POST'])
def sign_up():
    # 连接 MySQL 数据
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()

    #读取用户信息
    Uname = str(request.get_json()['Uname'])
    Upin = str(request.get_json()['Upin'])
    Utel = str(request.get_json()['Utel'])
    Uadd = str(request.get_json()['Uadd'])

    #将用户信息添加到用户表
    sql = "INSERT INTO USERS (Uname,Upin,Utel,Uadd,Umonny) VALUES (%s, %s, %s,%s,10000);"
    cursor.execute(sql,(Uname,Upin,Utel,Uadd))
    mydb.commit()
    success = {'success':True}
    cursor.close()
    mydb.close()
    return jsonify(success)


# 订单查询
@app.route('/person_search', methods=['POST'])
def person_search():
    # 连接 MySQL 数据
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()

    Uname = request.get_json()['Uname']
    sql = "SELECT Gname,Gquan FROM BUYINGS WHERE Uname=%s"
    cursor.execute(sql, (Uname,))
    buyings = cursor.fetchall()
    fields = ['Gname', 'Gquan']
    buyings_dict = [dict(zip(fields, row)) for row in buyings]
    
    cursor.close()
    mydb.close()
    # 构造响应对象
    response = {
        'success': True,
        'orders': buyings_dict
    }
    return jsonify(response)

#账户余额
@app.route('/get_yue', methods=['POST'])
def monny():
    # 连接 MySQL 数据
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()

    #读取用户姓名并查询金额
    Uname = str(request.get_json()['Uname'])
    sql = "SELECT Umonny FROM USERS WHERE Uname=%s"
    cursor.execute(sql,(Uname,))
    monny = cursor.fetchall()
    
    fields = ['Umonny']
    monny_dict = [dict(zip(fields, row)) for row in monny]
    # 构造响应对象
    response = {
        'success': True,
        'yue': monny_dict
    }
    cursor.close()
    mydb.close()
    return jsonify(response)

#购买功能
@app.route('/buy', methods=['POST'])
def buy():
    # 连接 MySQL 数据
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()

    #执行购买操作(库存修改)
    data = request.get_json()
    print(data)
    sql = 'UPDATE GOODS SET Gquan = Gquan - %s WHERE Gname = %s'
    for i in range(len(data)-1):
        cursor.execute(sql,(data[i]['quantity'],data[i]['name']))
        mydb.commit()
    
    #执行购买操作(用户余额修改)
    sql = 'UPDATE USERS SET Umonny = Umonny - %s WHERE Uname = %s'
    Uname = data[len(data)-1]['username']
    monny = data[len(data)-1]['price']
    cursor.execute(sql,(monny,Uname))
    mydb.commit()
    
    #用户订单修改
    sql = 'INSERT INTO BUYINGS(Uname,Gname,Gquan) VALUES(%s,%s,%s)'
    for i in range(len(data)-1):
        Gname = data[i]['name']
        Gquan = data[i]['quantity']
        cursor.execute(sql,(Uname,Gname,Gquan))
        mydb.commit()
    cursor.close()
    mydb.close()

    #构造响应对象
    success = {'success':True}
    return jsonify(success)
  
#购物车功能
@app.route('/cart', methods=['POST'])
def cart():
    # 连接 MySQL 数据
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()
    data = request.get_json()

    #添加购物车记录
    sql = 'INSERT INTO CART(Uname,Gname,Gquan) VALUES(%s,%s,%s)'
    Uname = data[len(data)-1]['username']
    for i in range(len(data)-2):
        Gname = data[i]['name']
        Gquan = data[i]['quantity']
        cursor.execute(sql,(Uname,Gname,Gquan))
    cursor.close()
    mydb.close()
    #构造响应对象
    success = {'success':True}
    return jsonify(success)
  


#搜索功能
@app.route("/search",methods=['POST'] )
def Buyname():
    # 连接 MySQL 数据
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()

    #按结果查询
    sql = "SELECT * FROM GOODS WHERE Gname LIKE CONCAT('%', %s, '%')"
    Gname = str(request.get_json()['Gname'])
    cursor.execute(sql, (Gname,))
    Gbuy = cursor.fetchall()

    fields = ['Gno','Gname','Gtype','Gprice','Gmark','Gquan','Gtime','Sname','Smark']
    Gbuy_dict = [dict(zip(fields, row)) for row in Gbuy]
    cursor.close()
    mydb.close()
    # 构造响应对象
    response = {
        'success': True,
        'products': Gbuy_dict
    }
    return jsonify(response)

#注销功能
@app.route('/delete', methods=['POST'])
def delete():
    # 连接 MySQL 数据
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()

    #删除用户数据
    Uname = str(request.get_json()['Uname'])
    sql = "DELETE FROM USERS WHERE Uname = %s;"
    cursor.execute(sql,(Uname,))
    mydb.commit()
    cursor.close()
    mydb.close()
    success = {'success':True}
    return jsonify(success)

#后台管理-商品删除
@app.route('/deleteProduct',methods=['POST'])
def delete_product():
    # 连接 MySQL 数据
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()
    Gno = int(request.get_json()['Gno'])
    sql = 'DELETE FROM GOODS WHERE Gno = %s;'
    cursor.execute(sql,(Gno,))
    mydb.commit()
    cursor.close()
    mydb.close()
    success = {'success':True}
    return jsonify(success)

#后台管理-商家删除
@app.route('/deleteShop',methods=['POST'])
def delete_shops():
    # 连接 MySQL 数据
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()
    Sno = request.get_json()['Sno']
    print(Sno)
    sql = 'DELETE FROM SHOPS WHERE Sno = %s'
    cursor.execute(sql,(Sno,))
    mydb.commit()
    cursor.close()
    mydb.close()
    success = {'success':True}
    return jsonify(success)

#后台管理-商家搜索
@app.route('/searchShops',methods=['POST'])
def search_shop():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()
    sql = 'SELECT * FROM SHOPS'
    cursor.execute(sql)
    shops = cursor.fetchall()
    mydb.commit()
    fields = ['Sno','Sname','Smark']
    shops_dict = [dict(zip(fields, row)) for row in shops]
    cursor.close()
    mydb.close()
    # 构造响应对象
    response = {
        'success': True,
        'shops': shops_dict
    }
    return jsonify(response)

#后台管理-商品搜索
@app.route('/searchProducts',methods=['POST'])
def search_product():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()
    sql = 'SELECT * FROM GOODS'
    cursor.execute(sql)
    goods = cursor.fetchall()
    mydb.commit()
    fields = ['Gno','Gname','Gtype','Gprice','Gmark','Gquan','Gtime','Sname','Smark']
    goods_dict = [dict(zip(fields, row)) for row in goods]
    cursor.close()
    mydb.close()
    # 构造响应对象
    response = {
        'success': True,
        'goods': goods_dict
    }
    return jsonify(response)

#后台管理-搜索用户
@app.route('/searchusers',methods=['POST'])
def search_users():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()
    sql = 'SELECT * FROM USERS'
    cursor.execute(sql)
    users = cursor.fetchall()
    fields = ['Uname','Upin','Utel','Uadd','Umonny']
    users_dict = [dict(zip(fields, row)) for row in users]
    cursor.close()
    mydb.close()
    # 构造响应对象
    response = {
        'success': True,
        'users': users_dict
    }
    return jsonify(response)

#后台管理-搜索订单
@app.route('/searchbuyings',methods=['POST'])
def search_buyings():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ustcshop"
    )
    cursor = mydb.cursor()
    sql = 'SELECT * FROM BUYINGS'
    cursor.execute(sql)
    buyings = cursor.fetchall()
    fields=['Uname','Gname','Gquan']
    buyings_dict = [dict(zip(fields, row)) for row in buyings]
    cursor.close()
    mydb.close()
    # 构造响应对象
    response = {
        'success': True,
        'buyings': buyings_dict
    }
    return jsonify(response)







    
    

# 运行Flask应用
if __name__ == '__main__':
    app.run()
