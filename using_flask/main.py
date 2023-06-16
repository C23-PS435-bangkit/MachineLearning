from flask import Flask, request, jsonify
from model import predict_image
from PIL import Image
from io import BytesIO
import requests

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json()

    # Extract the image URL from the JSON data
    image_url = data['image_url']

    # Download the image from the URL
    response = requests.get(image_url)
    response.raise_for_status()

    # Load the downloaded image directly from the response content
    image = Image.open(BytesIO(response.content))

    # Perform image prediction using the predict_image function
    prediction_results = predict_image(image)

    # Return the prediction results as JSON response
    return jsonify(prediction_results)

if __name__ == '__main__':
    app.run()
