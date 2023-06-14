import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input
from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

# Define the endpoint for face prediction
@app.route('/predict_face', methods=['POST'])
def predict_face():
    # Load the TensorFlow model
    model = tf.keras.models.load_model("model.h5", custom_objects={"KerasLayer": hub.KerasLayer})

    # Get the image file from the request
    image_file = request.files['image']

    # Read the image using OpenCV
    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Preprocess the image (e.g., resize, normalize, etc.)
    resized_image = cv2.resize(image, (224, 224))
    preprocessed_image = img_to_array(resized_image)
    preprocessed_image = preprocess_input(preprocessed_image)

    # Perform face prediction using the loaded model
    predictions = model.predict(np.array([preprocessed_image]))

    # Find the index with the highest probability
    max_index = np.argmax(predictions)

    # Get the class label associated with the index
    class_labels = ['Heart', 'Oblong', 'Oval', 'Round', 'Square']
    predicted_class = class_labels[max_index]

    # Prepare the response
    response = {
        'predicted_class': predicted_class,
        'probabilities': predictions.tolist()[0]
    }

    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    # Start the Flask application
    app.run()