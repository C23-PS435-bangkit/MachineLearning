// Load the models
const model1 = await tf.loadLayersModel('model1/model.json');
const model2 = await tf.loadLayersModel('model2/model.json');
const model3 = await tf.loadLayersModel('model3/model.json');

// Preprocess and predict image
async function predict_image(image) {
  const processedImage = preprocess(image);
  ``
  const prediction1 = model1.predict(processedImage);
  const prediction2 = model2.predict(processedImage);
  const prediction3 = model3.predict(processedImage);
  
  const result1 = prediction1.dataSync()[0];
  const result2 = prediction2.dataSync()[0];
  const result3 = prediction3.dataSync()[0];
  
  return [result1, result2, result3];
}

// Preprocess the image (adjust this function based on your preprocessing requirements)
function preprocess(image) {
  // Perform any preprocessing steps here (e.g., resizing, normalization)
  // Return the processed image as a tf.Tensor
  return tf.tensor(image);
}

// Example usage
const image = loadImage('path/to/image.jpg'); // Load your image here
predict_image(image).then((results) => {
  console.log(results); // Output the prediction results
});
