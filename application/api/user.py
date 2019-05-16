from application.api import app_user


# 视图函数
@app_user.route('/login')
def login():
    return '歡迎登陸'


@app_user.route('/register')
def register():
    return '歡迎注冊'
