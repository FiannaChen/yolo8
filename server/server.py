
import base64
import numpy as np
from PIL import Image
from detect import doDetect
import time
from flask import Flask, render_template, request, redirect
from flask_cors import CORS
app = Flask(__name__)
CORS(app)



@app.route("/", methods=["POST"])
def predict():
    #获取请求中的base64编码的图片
    base64_str = request.get_json().get("image")
    #解码
    img_data = base64.b64decode(base64_str)
    #保存图片文件
    
    file_name = str(time.time()) + ".jpg"
    with open(file_name, "wb") as f:
        f.write(img_data)
    #读取图片文件
    #调用detect函数进行预测
    result = doDetect(file_name)

    #返回预测结果
    return result
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)  # debug=True causes Restarting with stat
