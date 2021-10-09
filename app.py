import sqlite3
import pandas as pd
import os
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect ,render_template
con = sqlite3.connect('rober.db', check_same_thread=False)

UPLOAD_FOLDER = './image'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__,static_folder="./dist",template_folder = "./dist")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

'''


'''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET'])
# def home():
#     # cursor = con.execute("SELECT * from blog")
#     # temp = cursor.execute
#     # for i in cursor:
#     #     print(i)
#     df = pd.read_sql_query("SELECT id,TITLE,SUB_TITLE,KIND FROM blog", con=con)
#     print(df.to_dict('records'))
#     # return df.to_dict('records')
#     return 'test'

@app.route('/blog/all_List', methods=['GET'])
def home1():
    # cursor = con.execute("SELECT * from blog")
    # temp = cursor.execute
    # for i in cursor:
    #     print(i)
    df = pd.read_sql_query("SELECT id,TITLE,SUB_TITLE,KIND FROM blog", con=con)
    # return df.to_dict('records')
    return {"datas":df.to_dict('records')}
@app.route('/blog/<string:id>', methods=['GET'])
def home2(id):
    # cursor = con.execute("SELECT * from blog")
    # temp = cursor.execute
    # for i in cursor:
    #     print(i)

    df = pd.read_sql_query("SELECT id,TITLE,SUB_TITLE,KIND,HTML FROM blog WHERE ID ={}".format(id), con=con)
    print(df.to_dict('records'))
    # return df.to_dict('records')
    return {"datas":df.to_dict('records')}    

@app.route('/upload/image', methods=['GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            from flask import send_from_directory
            return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route("/", defaults={"fallback": ""})
@app.route("/<string:fallback>")
@app.route('/<path:fallback>')
def fallback(fallback):       # Vue Router 的 mode 为 'hash' 时可移除该方法
    if fallback.startswith('css/') or fallback.startswith('js/')\
            or fallback.startswith('img/') or fallback == 'favicon.ico':
        return app.send_static_file(fallback)
    else:
        return app.send_static_file('index.html')

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
