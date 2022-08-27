from flask import Flask,render_template,request,redirect
import config
import os

app = Flask(__name__)


# 主界面
@app.route('/')
def index():
    return render_template('index.html')

@app.before_request
def before_request():
    if request.url.startswith('http://'):
        url=request.url.replace('http://','https://',1)
        return redirect(url,code=301)

if __name__ == '__main__':
    pem_path = os.path.join(config.UPLOADED_PHOTOS_SSL, '8369638_lib61504.top.pem')
    pem_key = os.path.join(config.UPLOADED_PHOTOS_SSL, '8369638_lib61504.top.key')
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context=(pem_path, pem_key))
