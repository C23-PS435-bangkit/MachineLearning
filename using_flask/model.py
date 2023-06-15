import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import json

# Load the models
model_allergic = load_model('models/allergic vs non allergic/my_model.h5')
model_bacterial = load_model('models/bacterial vs non bacterial/model_bacterial.h5')
model_fungal = load_model('models/fungal vs non fungal/my_model.h5')
model_healthy = load_model('models/healthy vs non healthy/model_healthy.h5')

# Function to preprocess the image
def load_and_preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((128, 128))
    image = np.expand_dims(image, axis=0)
    image = image / 255.0  # Normalize the image
    return image

# Function to predict an image using all four models
def predict_image(image_path):
    # Load and preprocess the image
    image = load_and_preprocess_image(image_path)

    # Perform predictions using all four models
    prediction1 = model_allergic.predict(image)[0][0]
    prediction2 = model_bacterial.predict(image)[0][0]
    prediction3 = model_fungal.predict(image)[0][0]
    prediction4 = model_healthy.predict(image)[0][0]

    # Round the predictions and convert to binary status
    status2 = int(round(prediction2))
    status3 = int(round(prediction3))
    status1 = int(round(prediction1))
    status4 = int(round(prediction4))

    # Format the predictions as a dictionary
    results = {
        'model_allergic': {'prediction': float(prediction1), 'status': status1},
        'model_bacterial': {'prediction': float(prediction2), 'status': status2},
        'model_fungal': {'prediction': float(prediction3), 'status': status3},
        'model_healthy': {'prediction': float(prediction4), 'status': status4}
    }

    # results = {
    #     'model_allergic': {'prediction': float(prediction1), 'status': 1},
    #     'model_bacterial': {'prediction': float(prediction2), 'status': 0},
    #     'model_fungal': {'prediction': float(prediction3), 'status': 0},
    #     'model_healthy': {'prediction': float(prediction4), 'status': 0}
    # }

    if results['model_allergic']['status'] == 1 and results['model_bacterial']['status'] == 1 and results['model_fungal']['status'] == 1:
        diagnose = {
            'diagnose': 'Emergency',
            'treatment': "URGENT. Please bring your pet to nearest vetenarian as soon as possible!"
            }
    elif results['model_allergic']['status'] == 1:
        diagnose = {
            'diagnose' : 'Allergic',
            'treatment' : 'Depend on the allergy, the treatment might be different. please observe your pet allergic cause and provide healthy diet while also cleanse them with hypoallergenic shampoo. If the allergi keep getting worse please seek nearest vetenarian'
        }
    elif results['model_bacterial']['status'] == 1:
        diagnose = {
            'diagnose' : 'Bacterial',
            'treatment' : 'Please tend your beloved pet with medicated shampoos'
        }
    elif results['model_fungal']['status'] == 1:
        diagnose = {
            'diagnose': 'Fungal',
            'treatment' : 'Depending on fungal type, the treatment might be slightly different. For general treatment, please give your pet a antifungal shampoo and avoid letting your pet scratch the affected area'
        }
    elif results['model_allergic']['status'] == 0 and results['model_bacterial']['status'] == 0 and results['model_fungal']['status'] == 0:
        diagnose = {
            'diagnose': 'Healthy',
            'treatment': "Your pet is in good health. It is important to maintain your pet's healthy lifestyle by providing them a balanced diet, regular exercise, and keeping them up-to-date with vaccinations and preventive care. Regular check-ups with a veterinarian can help ensure that your pet stays healthy and can catch any potential issues early. Keep up the good work and continue to provide your pet with the love and care they deserve!"
            }
    # Convert the dictionary to JSON format
    json_results = diagnose

    return json_results
