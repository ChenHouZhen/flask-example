# 导入flask模块的Flask类
from flask import Flask ,flash
from flask import url_for
from flask import redirect
from user import user
from flask import request
from upload import upload


# 创建一个Flask类型的对象
# 参数解释
# import_name：                  指定应用的名字和工程目录，默认为__name__
# static_path=None：             是静态文件存放的路径，会赋值给static_url_path参数
# static_url_path=None：         设置静态文件路由的前缀，默认为“/static”
# static_folder='static'：       静态文件的存放目录， 默认值为"static"
# template_folder='templates':   模板文件的存放目录，默认值为"templates"
# instance_path=None:            设置配置文件的路径，在instance_relative_config=True情况下生效
# instance_relative_config=False:设置为True表示配置文件相对于实例路径而不是根路径
# root_path=None:  应用程序的根路径
app = Flask(__name__)

# 注册蓝本
app.register_blueprint(user)
app.register_blueprint(upload)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/log", methods=['GET', 'POST'])
def hi() -> str:
    app.logger.debug('-------------- DEBUG ----------------')
    app.logger.info('-------------- INFO ----------------')
    app.logger.error('-------------- ERROR ----------------')

    return "日志测试!"


# form-data 格式
@app.route('/params/form', methods=['POST'])
def params_form():
    app.logger.debug('-------------- params form --------------')
    app.logger.debug('params ==> {}:{}'.format('params1', request.form['params1']))
    app.logger.debug('params ==> {}:{}'.format('params2', request.form['params2']))
    return "调用成功"


# application/json 格式
@app.route('/params/json', methods=['POST'])
def params_json():
    app.logger.debug('-------------- params json --------------')
    app.logger.debug('params ==> {}:{}'.format('params1', request.json['params1']))
    app.logger.debug('params ==> {}:{}'.format('params2', request.json['params2']))
    return "调用成功"


# url_for() 获取指定方法名的 请求路径
@app.route('/url_for', methods=['GET'])
def url_for_log():
    print(url_for('hi'))


# redirect() 重定向
@app.route('/redirect')
def re():
    return redirect('https://www.baidu.com')


if __name__ == '__main__':
    # 参数解释
    # host :  IP
    # port :  端口
    app.run()
