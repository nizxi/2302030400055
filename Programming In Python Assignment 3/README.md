🧠 MNIST Digit Classifier using TensorFlow

This mini-project demonstrates how to build a Convolutional Neural Network (CNN) using TensorFlow to classify handwritten digits from the MNIST dataset. The MNIST dataset contains 70,000 grayscale images of handwritten digits (0–9), each sized 28x28 pixels.

📌 Step-by-Step Breakdown

🔹Step 1: Import Libraries

We start by importing the required modules from TensorFlow:

import tensorflow as tf
from tensorflow.keras import layers, models

tensorflow: Core library for deep learning.

layers: Used to define the CNN architecture.

models: Allows us to stack layers in a Sequential model.

🔹Step 2: Load and Preprocess the Dataset

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

Normalize the pixel values to the range [0, 1]
x_train, x_test = x_train / 255.0, x_test / 255.0

mnist.load_data(): Loads the dataset.

Data is normalized so that each pixel is between 0 and 1, which speeds up training.

🔹Step 3: Build the Neural Network Model

We use a Convolutional Neural Network for better image feature extraction.

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

Model Architecture:

Conv2D + MaxPooling: Extract spatial features from the image.

Flatten: Converts 2D features into a 1D vector.

Dense: Fully connected layers.

Dropout: Prevents overfitting.

Softmax: Outputs probability distribution over 10 digit classes.

Note: Before training, reshape x_train and x_test to include the channel dimension:

x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

🔹Step 4: Compile the Model

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

adam: Adaptive optimizer that works well for most problems.

sparse_categorical_crossentropy: Suitable for integer-labeled classification.

accuracy: Metric used to evaluate the model.

🔹Step 5: Train the Model

model.fit(x_train, y_train, epochs=5)

Trains the model on training data for 5 epochs.

Each epoch runs through the entire dataset once.

Sample Output:

Epoch 1/5 - accuracy: 0.8085 - loss: 0.5787
Epoch 2/5 - accuracy: 0.9724 - loss: 0.0954
...
Epoch 5/5 - accuracy: 0.9894 - loss: 0.0388

✅ Result

The model achieves over 99% accuracy after just 5 epochs, making it a strong baseline for handwritten digit classification tasks.

