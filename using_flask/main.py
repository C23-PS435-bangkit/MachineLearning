from flask import Flask, request, jsonify
from model import predict_image
import os


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    file = request.files['image']

    # Save the image to a temporary file
    image_path = 'temp_image.jpg'
    file.save(image_path)

    # Perform image prediction using the predict_image function
    prediction_results = predict_image(image_path)

    # Delete the temporary image file
    os.remove(image_path)

    # Return the prediction results as JSON response
    return jsonify(prediction_results)

if __name__ == '__main__':
    app.run()