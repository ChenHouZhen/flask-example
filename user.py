from flask import Blueprint, url_for

# 创建对象，可以指定统一的前缀
user = Blueprint('user', __name__, url_prefix='/user')


# 视图函数
@user.route('/login')
def login():
    return '歡迎登陸'


@user.route('/register')
def register():
    return '歡迎注冊'
