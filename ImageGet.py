import base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def imageget():
    ImageBase64 = request.form['ImageBase64']
    with open("CatImage.png", "wb") as Image:
        Image.write(base64.decodebytes(ImageBase64))
    return 'Success!'


if __name__ == '__main__':
    app.run()
