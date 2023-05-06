from datetime import timedelta
from flask import Flask, render_template, url_for, flash, redirect, request, session
import pymysql
import jinja2

app = Flask(__name__)
app.secret_key='12345qwert'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)  # 设置会话的持续时间（这里设置为 5 分钟）
app.config['SESSION_PERMANENT'] = False  # 设置会话在浏览器关闭时过期

@app.route("/")
def home():
    #重定向“/”到登录页面
    return redirect(url_for("login"))

@app.route('/index')
def index():
    if 'username' not in session:
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 实现登录逻辑
        username = request.form['username']
        password = request.form['password']

        user = authenticate_user(username, password)
        
        if user:
            session['username'] = user['username']
            return render_template("index.html")
        else:
           flash("用户名或密码错误,请重新登录")
    return render_template("login.html")



def authenticate_user(username, password):
    #登陆验证
    connection = pymysql.connect(
        host='43.140.253.7',
        user='root',
        password='Shy990428!',
        database='shy',
        port=22704
    )
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE user_name = %s AND password = %s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()
            if result:
                result_dict = {
                    'username' : result[0],
                    'password' : result[1]
                }
                return result_dict
    finally:
        connection.close()


if __name__ == "__main__":
    app.run(debug=True)



