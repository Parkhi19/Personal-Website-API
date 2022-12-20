from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask_cors import CORS, cross_origin

# Use a service account.
cred = credentials.Certificate('./credentials.json')

firebaseApp = firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/get/all-blogs')
@cross_origin()
def get_all_blogs():
    allBlogs = db.collection("blogs").stream()
    aB = list()
    for blog in allBlogs:
        aB.append(blog.to_dict())
    return jsonify({"data": aB})


@app.route('/get/personal-info')
@cross_origin()
def get_personal_info():
    personalInfo = db.collection("personal-info").document("0YvBob1h41L2aWMNoxNU").get()
    return jsonify({"data": personalInfo.to_dict()})


@app.route('/get/know-more-content')
@cross_origin()
def get_know_more_content():
    getKnowMoreContent = db.collection("personal-info").document("ZRK0ovY4QwgkeBIKKQto").get()
    return jsonify({"data":getKnowMoreContent.to_dict()})


if __name__ == '__main__':
    app.run()
