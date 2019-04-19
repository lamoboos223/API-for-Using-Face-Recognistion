from flask import Flask
from flask import request
import face_recognition

app = Flask(__name__)


@app.route('/Images', methods=['POST'])
def POST():
    if request.method == 'POST':

        # getting the images url from the request
        name1 = request.form.get('name1')
        name2 = request.form.get('name2')

        # map the url to the ones in the folder images
        firstImage = "images/" + name1
        secondImage = "images/" + name2

        # loading the image inside a variable
        firstImage = face_recognition.load_image_file(firstImage)
        secondImage = face_recognition.load_image_file(secondImage)

        # encode the images
        firstImage = face_recognition.face_encodings(firstImage)[0]
        secondImage = face_recognition.face_encodings(secondImage)[0]

        # compare the two encoded images
        result = face_recognition.compare_faces([firstImage], secondImage)

        # returning the final result
        if result[0] == True:
            return "True"
        else:
            return "False"


if __name__ == "__main__":
    app.run(debug=True)
