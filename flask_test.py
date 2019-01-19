#MUST make sure to "export FLASK_APP={file_name}" in terminal before running "flask run"
#use "export FLASK_DEBUG=1" in order to turn on debug mode (automatic update from code)
# Sources of Help: https://www.youtube.com/watch?v=QnDWIZuWYW0&m=19

from flask import Flask, render_template
import io
app = Flask(__name__) #__name__ just means the name of module in python

updates = [
  {
    'author': 'Antony Nguyen',
    'title': 'This Project Sucks',
    'content': 'Good riddance, I\'m being toxic. ',
    'date_posted': '10/31/18'
  },
  {
    'author': 'William Martino',
    'title': 'Butt Plugs Rule!',
    'content': 'Can we please just make a butt plug. ',
    'date_posted': '11/01/18'
  },

]

def detect_faces(uri):
    """Detects faces in an images"""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    # image = vision.types.Image()
    # image.source.image_uri = uri

    with io.open(uri, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

    print ('Faces:')
    for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))

testPath = "images/canada-head.jpg"
detect_faces(testPath)

@app.route("/") #pathway of url
@app.route("/home")
def home():
    return render_template('home.html', updates = updates) #var is same name as var in html

@app.route("/about") #pathway of url
def about():
    return render_template('about.html', title = "About")

#allows app to run & turns debug mode on using Python (w/o bash)
#__main__ is the name of the main module that runs (kinda like main method in Java)
if __name__ == '__main__':
    app.run(debug=True)
