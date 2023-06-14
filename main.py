from flask import Flask, request, jsonify
import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the TensorFlow model
model = tf.keras.models.load_model("model.h5")

# Define the endpoint for face prediction
@app.route('/predict_face', methods=['POST'])
def predict_face():
    # Get the image file from the request
    image_file = request.files['image']

    # Read the image using OpenCV
    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Preprocess the image (e.g., resize, normalize, etc.)
    # ...

    # Perform face prediction using the loaded model
    predictions = model.predict(np.array([image]))
    
    # Find the index with the highest probability
    max_index = np.argmax(predictions)

    # Get the class label associated with the index
    class_labels = ['Heart', 'Oblong', 'Oval', 'Round', 'Square']
    predicted_class = class_labels[max_index]

    # Process the predictions and prepare the response
    # ...
    response = {
        'predicted_class': predicted_class,
        'probabilities': predictions.tolist()[0]  # Convert numpy array to a list
    }

    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    # Start the Flask application
    app.run()aa