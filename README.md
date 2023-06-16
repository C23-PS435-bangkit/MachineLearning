# Model Testing with Flask

This repository provides a Flask application for testing a machine learning model. Follow the steps below to set up the environment and test the model.

## Prerequisites

- Python 3.x
- pip
- Postman (for testingn purposes)

## Steps

1. Clone the repository:
    ```
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ````
2. Since the only working model is in flask, change the working directory into `using_flask`:
    ```
    cd using_flask
    ```
3. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/Scripts/activate
    ```
4. Create a virtual environment
    ```
    python -m venv venv
    source venv/Scripts/activate
    ```
5. Start the Flask application:
    ```
    python main.py
    ```
6. Open the postman and enter the value of URL using POST methods of
    ```
    http://localhost:5000 (Will be changed later teehe)
    ```
    and the request body using raw (JSON type)
    ```
    {
        "image_url": "<<Insert your pic url>>"
    }
    ```
7. The application will download the image, process it using the machine learning model, and display the prediction results.
8. Test the model with different image URLs to observe the predictions.
9. When finished, press Ctrl + C in the terminal to stop the Flask application.

## Additional Information
- The Flask application code can be found in app.py.
- The machine learning model code is imported from the model.py file
- Modify the code as needed to fit your specific machine learning model and requirements.
- Ensure that the required modules are correctly installed to avoid any dependency issues.
