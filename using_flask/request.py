import requests
import os

# URL of your Flask API
url = 'http://127.0.0.1:5000/predict'  # Update with your API URL

# Directory containing the images
image_dir = 'images'  # Update with the actual image directory

# Iterate through the images in the directory
for image_file in os.listdir(image_dir):
    image_path = os.path.join(image_dir, image_file)

    # Create a dictionary with the image file
    files = {'image': open(image_path, 'rb')}

    # Make the POST request
    response = requests.post(url, files=files)

    # Check the response
    if response.status_code == 200:
        # Print the image's name and the API output
        print('Image:', image_file)
        print('API Output:', response.json())
        print()
    else:
        # Print the error message
        print('Error:', response.text)
