const tf = require('@tensorflow/tfjs-node');
const os = require('os');
const path = require('path');

const loadModel = async () => {
    const model = await tf.loadLayersModel('file://' + path.join(__dirname, 'models/allergic vs non allergic/model.json'))
}

// await tf.loadLayersModel('D:\6th SEMESTER\BANGKIT\Repo\MachineLearning\models\allergic vs non allergic\model.json');