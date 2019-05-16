import os
from flask import render_template, request, jsonify ,make_response, send_file
import time
from application.main.bill import Bill
from application.api import app_upload


UPLOAD_FOLDER = 'upload'
# upload.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # 设置文件上传的目标文件夹
basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前项目的绝对路径
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF'])  # 允许上传的文件后缀


# 判断文件是否合法
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 具有上传功能的页面
@app_upload.route('/page')
def upload_test():
    return render_template('upload.html')


@app_upload.route('/api/upload', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, UPLOAD_FOLDER)  # 拼接成合法文件夹地址
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)  # 文件夹不存在就创建
    f=request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname=f.filename
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename = str(unix_time)+'.'+ext   # 修改文件名
        new_filename = os.path.join(file_dir, new_filename)
        f.save(new_filename)  #保存文件到upload目录

        b = Bill()
        result_filename = b.get_result(new_filename)
        response = make_response(send_file(result_filename))
        response.headers["Content-Disposition"] = "attachment; filename={}".format("文件.jpg".encode().decode('latin-1'))
        return response
    else:
        return jsonify({"errno": 1001, "errmsg": "上传失败"})
