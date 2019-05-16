from flask import Blueprint
# 创建对象，可以指定统一的前缀
app_upload = Blueprint('upload', __name__, url_prefix='/upload')


# 创建对象，可以指定统一的前缀
app_user = Blueprint('user', __name__, url_prefix='/user')
