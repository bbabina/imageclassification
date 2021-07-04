from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/classify_image', methods = ['GET', 'POST'])
def classify_image():
    return "hi"

if __name__ == '__main__':
    app.run(port=5000)

# image to base64 -> converts any image to string