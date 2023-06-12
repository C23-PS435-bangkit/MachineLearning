import requests

# URL of your Flask API
url = 'http://127.0.0.1:5000/predict'  # Update with your API URL

# Path to the image file
image_path = 'images\example_allergic.jpg'  # Update with the actual image path

# Create a dictionary with the image file
files = {'image': open(image_path, 'rb')}

# Make the POST request
response = requests.post(url, files=files)

# Check the response
if response.status_code == 200:
    # Print the prediction results
    print(response.json())
else:
    # Print the error message
    print('Error:', response.text)