from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/review', methods=['GET'])
def listing():

    html_css = list(db.coding.find({'title': 'Html/Css'}, {'_id': False}))
    return jsonify({'all_coding': html_css})

    # JS = list(db.coding.find({'title': 'JavaScript'}, {'_id': False}))
    # return jsonify({'all_coding': JS})
    #
    # java = list(db.coding.find({'title': 'java'}, {'_id': False}))
    # return jsonify({'all_coding': java})
    #
    # react = list(db.coding.find({'title': 'React'}, {'_id': False}))
    # return jsonify({'all_coding': react})
    #
    # node = list(db.coding.find({'title': 'node.js'}, {'_id': False}))
    # return jsonify({'all_coding': node})
    #
    # jquery = list(db.coding.find({'title': 'jquery'}, {'_id': False}))
    # return jsonify({'all_coding': jquery})
    #
    # spring = list(db.coding.find({'title': 'spring'}, {'_id': False}))
    # return jsonify({'all_coding': spring})
    #
    # vue = list(db.coding.find({'title': 'vue.js'}, {'_id': False}))
    # return jsonify({'all_coding': vue})
    #
    # python = list(db.coding.find({'title': 'python'}, {'_id': False}))
    # return jsonify({'all_coding': python})
    #
    # C_C = list(db.coding.find({'title': 'c/c++'}, {'_id': False}))
    # return jsonify({'all_coding': C_C})
    #
    # etc = list(db.coding.find({'title': 'etc'}, {'_id': False}))
    # return jsonify({'all_coding': etc})



# html/css, javascript, java, react, node.js, jquery, spring, vue.js, python, c/c++,etc

## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def saving():
    title_receive = request.form['title_give']
    url_receive = request.form['url_give']
    review_receive = request.form['review_give']
    lecture_receive = request.form['lecture_give']



    # 저장 - 예시
    doc = {'title': title_receive,
           'url': url_receive,
           'review': review_receive,
           'lecture': lecture_receive,
           }
    db.coding.insert_one(doc)

    return jsonify({'msg':'post success!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)