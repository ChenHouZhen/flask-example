from ext import db
from models import Role, User
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Command


class Hello(Command):

    def run(self):
        print("Hello world")


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Fianna'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 绑定数据库
db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)

# 集成数据库迁移命令，步骤1执行一次即可，需要修改数据模型后需要迁移执行2、3步骤即可
# 1.创建迁移仓库：python manage.py db init
# 2.创建迁移脚本：python manage.py db migrate --message "initial migration"
# 3.更新数据库：python manage.py db upgrade
# MigrateCommand是flask-migrate集成的一个命令
manager.add_command('db', MigrateCommand)
manager.add_command('hello', Hello())


@manager.command
def ping():
    print("ping")


# 傳入參數
@manager.option('-n', '--name', help='Your name')
def name(name):
    print("hello", name)


# 創建所有表
@app.route('/create')
def create_all_tables():
    db.create_all()
    return "創建成功"


# 刪除所有表
@app.route('/drop')
def drop_all_tables():
    db.drop_all()
    return "刪除成功"


# 插入單行
@app.route('/insert')
def insert():
    db.session.add(Role(name='Admin'))
    db.session.commit()
    return "插入成功"


# 插入多行
@app.route('/insert_multi')
def insert_multi():
    db.session.add_all([User(username='john', role_id=1),
                        User(username='susan', role_id=3),
                        User(username='david',role_id=3)])
    db.session.commit()
    return "插入成功"


# 更新行
@app.route('/update')
def update():
    admin = Role.query.filter_by(name='Admin').first()
    admin.name = 'Administrator'
    db.session.commit()
    return '更新成功'


# 刪除單行
@app.route('/delete')
def delete():
    mod = Role.query.filter_by(name='Moderator').first()
    db.session.delete(mod)
    db.session.commit()
    return '刪除成功'


# 查詢表
@app.route('/select_all')
def select_all():
    print(Role.query.all())
    return '查詢成功'


# 查詢表
# 多個條件可以寫在 id=2 後面 ，如 id=2,name='Admin'
@app.route('/select_filter')
def select_filter():
    print(Role.query.filter_by(id=2).all())
    return '查詢成功'


if __name__ == '__main__':
    manager.run()