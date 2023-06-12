import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import json

# Load the models
model_allergic  = load_model('models/allergic vs non allergic/my_model.h5')
model_bacterial = load_model('models/bacterial vs non bacterial/model_bacterial.h5')
model_fungal    = load_model('models/fungal vs non fungal/my_model.h5')
model_healthy   = load_model('models\healthy vs non healthy\model_healthy.h5')

# Function to predict an image using all four models
def predict_image(image_path):
    # Load and preprocess the image
    image = load_and_preprocess_image(image_path)

    # Perform predictions using all four models
    prediction1 = model_allergic.predict(image)[0][0]
    prediction2 = model_bacterial.predict(image)[0][0]
    prediction3 = model_fungal.predict(image)[0][0]
    prediction4 = model_healthy.predict(image)[0][0]

    # Format the predictions as a dictionary
    results = {'model_allergic': float(prediction1),
               'model_bacterial': float(prediction2),
               'model_fungal': float(prediction3),
               'model_healthy': float(prediction4)}

    # Convert the dictionary to JSON format
    json_results = json.dumps(results)

    return json_results

# Function to load and preprocess the image
def load_and_preprocess_image(image_path):
    # Load the image using your preferred method (e.g., PIL, OpenCV)
    # Preprocess the image as needed (e.g., resize, normalize)

    # Load the image using PIL
    image = Image.open(image_path)

    # Preprocess the image (resize, normalize, etc.)
    image = image.resize((128, 128))  # Example: Resize the image to (224, 224)
    image = np.array(image) / 255.0  # Example: Normalize pixel values between 0 and 1

    # Return the preprocessed image as a numpy array
    return np.expand_dims(image, axis=0)

