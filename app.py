from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient

import requests

app = Flask(__name__)

client = MongoClient('3.36.111.59', 27017, username="test", password="test")
db = client.project_01


@app.route('/')
def main():

    return render_template("index.html")


# 로그인 페이지
@app.route('/login/')
def detail():
    return render_template("login.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)





# 아래는 코딩 참고용 상세페이지에는 app.py 코딩 없음

# @app.route('/')
# def home():
#    return render_template('index.html')
#
# @app.route('/memo', methods=['GET'])
# def listing():
#     sample_receive = request.args.get('sample_give')
#     print(sample_receive)
#     return jsonify({'msg':'GET 연결되었습니다!'})
#
# ## API 역할을 하는 부분
# @app.route('/memo', methods=['POST'])
# def saving():
#     sample_receive = request.form['sample_give']
#     print(sample_receive)
#     return jsonify({'msg':'POST 연결되었습니다!'})
#
# if __name__ == '__main__':
#    app.run('0.0.0.0',port=5000,debug=True)