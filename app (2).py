from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/html_css')
def html1():
    return render_template('html_css.html')


@app.route('/js')
def js1():
    return render_template('js.html')


@app.route('/java')
def java1():
    return render_template('java.html')


@app.route('/react_vue')
def react_vue1():
    return render_template('react_vue.html')


@app.route('/node')
def node1():
    return render_template('node.html')


@app.route('/jquery')
def jquery1():
    return render_template('jquery.html')


@app.route('/spring')
def spring1():
    return render_template('spring.html')


@app.route('/python')
def python1():
    return render_template('python.html')


@app.route('/c_c')
def c_c1():
    return render_template('c_c.html')


@app.route('/etc')
def etc1():
    return render_template('etc.html')


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

    return jsonify({'msg': 'post success!'})


@app.route('/review', methods=['GET'])
def readReviews():
    reviews = list(db.coding.find({}, {'_id': False}))
    return jsonify({'all_reviews': reviews})


@app.route('/html_css_review', methods=['GET'])
def listing():
    html_css = list(db.coding.find({'lecture': 'html'}, {'_id': False}))
    return jsonify({'html_css_reviews': html_css})


@app.route('/js_review', methods=['GET'])
def listing1():
    js = list(db.coding.find({'lecture': 'JavaScript'}, {'_id': False}))
    return jsonify({'js_reviews': js})


@app.route('/java_review', methods=['GET'])
def listing2():
    java = list(db.coding.find({'lecture': 'Java'}, {'_id': False}))
    return jsonify({'java_reviews': java})


@app.route('/react_vue_review', methods=['GET'])
def listing3():
    react_vue = list(db.coding.find({'lecture': 'React,Vue.js'}, {'_id': False}))
    return jsonify({'react_vue_reviews': react_vue})


@app.route('/node_review', methods=['GET'])
def listing4():
    node = list(db.coding.find({'lecture': 'Node.js'}, {'_id': False}))
    return jsonify({'node_reviews': node})


@app.route('/jquery_review', methods=['GET'])
def listing5():
    jquery = list(db.coding.find({'lecture': 'jQuery'}, {'_id': False}))
    return jsonify({'jquery_reviews': jquery})


@app.route('/spring_review', methods=['GET'])
def listing6():
    spring = list(db.coding.find({'lecture': 'Spring'}, {'_id': False}))
    return jsonify({'spring_reviews': spring})


@app.route('/python_review', methods=['GET'])
def listing7():
    python = list(db.coding.find({'lecture': 'Python'}, {'_id': False}))
    return jsonify({'python_reviews': python})


@app.route('/c_c_review', methods=['GET'])
def listing8():
    c_c = list(db.coding.find({'lecture': 'C,C++'}, {'_id': False}))
    return jsonify({'c_c_reviews': c_c})


@app.route('/etc_review', methods=['GET'])
def listing9():
    etc = list(db.coding.find({'lecture': 'ETC'}, {'_id': False}))
    return jsonify({'etc_reviews': etc})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)