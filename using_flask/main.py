from flask import Flask, request, jsonify
from model import predict_image
import os
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

    # Save the downloaded image to a temporary file
    image_path = 'temp_image.jpg'
    with open(image_path, 'wb') as file:
        file.write(response.content)

    # Perform image prediction using the predict_image function
    prediction_results = predict_image(image_path)

    # Delete the temporary image file
    os.remove(image_path)

    # Return the prediction results as JSON response
    return jsonify(prediction_results)

if __name__ == '__main__':
    app.run()


# @app.route('/save-diagnose',methods=['POST'])
# def save-diaAgnose():

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the image file from the request
#     file = request.files['images']
#     # Save the image to a temporary file.
#     image_path = 'temp_image.jpg' 
#     file.save(image_path)

#     # Perform image prediction using the predict_image function
#     prediction_results = predict_image(image_path)

#     # Delete the temporary image file
#     os.remove(image_path)

#     # Return the prediction results as JSON response
#     return jsonify(prediction_results)
# #is allergic

# # @app.route('/save-diagnose',methods=['POST'])
# # def save-diaAgnose():



if __name__ == '__main__':
    app.run()