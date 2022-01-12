<<<<<<< HEAD
from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
# 리뷰작성하는 부분
@app.route('/review', methods=['POST'])
def makeReview():
    title_receive = request.form['title_give']
    url_receive = request.form['url_give']
    review_receive = request.form['review_give']
    lecture_receive = request.form['lecture_give']

    doc = {
        'title': title_receive,
        'url': url_receive,
        'review': review_receive,
        'lecture': lecture_receive
    }
    db.lecture_review.insert_one(doc)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'msg': '리뷰가 성공적으로 작성되었습니다.'})


# 리뷰 보여주는 부분
@app.route('/review', methods=['GET'])
def readReviews():
    reviews = list(db.lecture_review.find({}, {'_id': False}))
    return jsonify({'all_reviews': reviews})


if __name__ == '__main__':
=======
from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
# 리뷰작성하는 부분
@app.route('/review', methods=['POST'])
def makeReview():
    title_receive = request.form['title_give']
    url_receive = request.form['url_give']
    review_receive = request.form['review_give']
    lecture_receive = request.form['lecture_give']

    doc = {
        'title': title_receive,
        'url': url_receive,
        'review': review_receive,
        'lecture': lecture_receive
    }
    db.lecture_review.insert_one(doc)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'msg': '리뷰가 성공적으로 작성되었습니다.'})


# 리뷰 보여주는 부분
@app.route('/review', methods=['GET'])
def readReviews():
    reviews = list(db.lecture_review.find({}, {'_id': False}))
    return jsonify({'all_reviews': reviews})


if __name__ == '__main__':
>>>>>>> b5db678751d45998bd9b978745beec0cf5e0ec0e
    app.run('0.0.0.0', port=5000, debug=True)