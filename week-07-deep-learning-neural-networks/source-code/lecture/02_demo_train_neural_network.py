"""
Train a small neural network with Fashion MNIST

This script is the second Week 7 lecture demo.
It shows the basic neural-network workflow:
- Load and prepare image data.
- Build a small Keras model.
- Compile the model.
- Train the model.
- Evaluate it on test data.
- Visualize training history and prediction examples.

This is still a learning demo. Neural networks are useful in some situations, but
they are not automatically better than simpler models.
"""

import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Reduce TensorFlow system messages so the lecture output stays easier to read.
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")

import tensorflow as tf

from utils import fashion_mnist_class_names, load_fashion_mnist

# ----------------------------------------------------------------------------------------
# Path handling: reliably locate files relative to this script
# ----------------------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
OUTPUTS_DIR = BASE_DIR / "outputs"

OUTPUTS_DIR.mkdir(exist_ok=True)

# ----------------------------------------------------------------------------------------
# Reproducibility: make results more stable between runs
# ----------------------------------------------------------------------------------------

# Neural-network training includes random starting values.
# A seed helps make the demo output more similar each time we run it.
tf.keras.utils.set_random_seed(42)

# ----------------------------------------------------------------------------------------
# Step 1: Load the dataset
# ----------------------------------------------------------------------------------------

# Fashion MNIST gives us enough image data for a small neural-network demo.
# The images are already labeled and all have the same shape: 28 x 28 pixels.
(train_images, train_labels), (test_images, test_labels) = load_fashion_mnist()

# `fashion_mnist_class_names` comes from utils.py.
# It lets us turn numeric predictions like 9 into readable labels like "Ankle boot".
print("--- Dataset shapes ---")
print("Training images:", train_images.shape)
print("Training labels:", train_labels.shape)
print("Test images:", test_images.shape)
print("Test labels:", test_labels.shape)

# ----------------------------------------------------------------------------------------
# Step 2: Prepare the data
# ----------------------------------------------------------------------------------------

# Image pixels are numbers from 0 to 255.
# Neural networks often train better when input values are smaller and consistent.
# Dividing by 255.0 changes the range from 0.0 to 1.0.
train_images = train_images / 255.0
test_images = test_images / 255.0

print("\n--- Normalized image values ---")
print("Smallest training pixel value:", train_images.min())
print("Largest training pixel value:", train_images.max())

# ----------------------------------------------------------------------------------------
# Step 3: Build a small neural network
# ----------------------------------------------------------------------------------------

# `Sequential` means the model is a simple stack of layers.
# This is a good first format because we can read it from top to bottom.
model = tf.keras.Sequential(
    [
        # The input layer tells Keras the shape of one image.
        tf.keras.Input(shape=(28, 28), name="input_layer_image"),

        # Flatten turns a 28 x 28 image into one long list of 784 numbers.
        # It does not learn patterns by itself. It only reshapes the data.
        tf.keras.layers.Flatten(name="input_layer_flatten"),

        # Dense means every neuron in this layer receives all values from the previous layer.
        # 128 neurons is a reasonable small demo size.
        # ReLU is an activation function that helps the model learn non-linear patterns.
        tf.keras.layers.Dense(128, activation="relu", name="hidden_layer_1"),

        # Optional idea: try 256 neurons instead of 128.
        # More neurons can learn more, but can also train slower and overfit more easily.
        # tf.keras.layers.Dense(256, activation="relu", name="hidden_layer_1"),

        # Optional idea: Dropout can sometimes reduce overfitting.
        # We skip it in the clean first version to keep the workflow easier to follow.
        # tf.keras.layers.Dropout(0.2, name="dropout_after_hidden_1"),

        # The output layer has 10 neurons because Fashion MNIST has 10 classes.
        # Softmax turns the output into probability-like scores that add up to 1.
        tf.keras.layers.Dense(10, activation="softmax", name="output_layer"),
    ],
    name="fashion_mnist_classifier",
)

print("\n--- Model summary ---")

# `model.summary()` prints a table of the model structure.
# It helps us check that the layers are connected in the order we expected.
# Useful things to point out:
# - Layer: the name and type of each layer.
# - Output Shape: what shape the data has after that layer.
# - Param #: how many trainable values the model needs to learn in that layer.
# More parameters can make a model more powerful but also heavier and easier to overfit.
model.summary()

# ----------------------------------------------------------------------------------------
# Step 4: Compile the model
# ----------------------------------------------------------------------------------------

# Compile chooses how the model will learn and how we will measure progress.
# - optimizer: how the model updates its weights.
# - loss: how the model measures wrong predictions during training.
# - metrics: extra values we want to see, such as accuracy.
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

# `sparse_categorical_crossentropy` fits this dataset because:
# - We have more than two classes.
# - The labels are numbers like 0, 1, 2, not one-hot encoded lists.

# ----------------------------------------------------------------------------------------
# Step 5: Train the model
# ----------------------------------------------------------------------------------------

# `fit` means the model learns from the training data.
# `epochs=5` means the model sees the full training set five times.
# `validation_split=0.1` holds back 10% of the training data for a validation check.
# This helps us notice if the model improves on training data but not on unseen data.
# `verbose=2` prints one clean line per epoch.
# If you want the animated progress bar instead, try `verbose=1`.
history = model.fit(
    train_images,
    train_labels,
    epochs=5,
    validation_split=0.1,
    verbose=2,
)

# ----------------------------------------------------------------------------------------
# Step 6: Evaluate the model
# ----------------------------------------------------------------------------------------

# The test set is separate data that the model did not train on.
# This gives us a more honest check than only looking at training accuracy.
test_loss, test_accuracy = model.evaluate(test_images, test_labels, verbose=0)

print("\n--- Test results ---")
print(f"Test loss: {test_loss:.4f}")
print(f"Test accuracy: {test_accuracy:.4f}")

# ----------------------------------------------------------------------------------------
# Step 7: Make predictions
# ----------------------------------------------------------------------------------------

# `predict` returns one list of 10 scores for each image.
# The highest score is the model's predicted class.
predictions = model.predict(test_images, verbose=0)

print("\n--- First prediction scores ---")
print(predictions[0].round(3))

# ----------------------------------------------------------------------------------------
# Step 8: Plot the training history
# ----------------------------------------------------------------------------------------

# The history object stores the accuracy and validation accuracy for each epoch.
# If training accuracy rises but validation accuracy stops improving, that can be a
# sign of overfitting. Overfitting means the model learned the training data too
# specifically and may not generalize as well to new data.
accuracy_values = history.history["accuracy"]
validation_accuracy_values = history.history["val_accuracy"]
epochs = range(1, len(accuracy_values) + 1)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(epochs, accuracy_values, marker="o", label="train_accuracy")
ax.plot(epochs, validation_accuracy_values, marker="o", label="val_accuracy")

ax.set_title("Training and Validation Accuracy")
ax.set_xlabel("Epoch")
ax.set_ylabel("Accuracy")
ax.legend()

plt.tight_layout()
fig.savefig(OUTPUTS_DIR / "fashion_mnist_training_accuracy.png")
plt.show()
plt.close(fig)

# ----------------------------------------------------------------------------------------
# Step 9: Show prediction examples
# ----------------------------------------------------------------------------------------

# We show 12 images because they fit nicely in a 3 x 4 grid.
# This is not a special machine-learning number.
number_of_prediction_examples = 12

print("\n--- Prediction grid ---")
print(
    f"Showing the first {number_of_prediction_examples} test images "
    "with predicted labels and true labels."
)

fig, axes = plt.subplots(3, 4, figsize=(12, 8))
fig.suptitle(
    f"First {number_of_prediction_examples} Test Predictions\n"
    "Predicted Label Compared With True Label",
    fontsize=14,
)

for index, ax in enumerate(axes.flat[:number_of_prediction_examples]):
    ax.imshow(test_images[index], cmap=plt.cm.binary)

    # `np.argmax` returns the index of the largest value.
    # Here it gives us the class with the highest prediction score.
    predicted_label_index = np.argmax(predictions[index])
    predicted_label = fashion_mnist_class_names[predicted_label_index]
    true_label = fashion_mnist_class_names[test_labels[index]]

    title_text = f"Pred: {predicted_label}\nTrue: {true_label}"
    ax.set_title(title_text, fontsize=9)
    ax.axis("off")

plt.tight_layout(rect=(0, 0, 1, 0.92))
fig.savefig(OUTPUTS_DIR / "fashion_mnist_prediction_examples.png")
plt.show()
plt.close(fig)

# ----------------------------------------------------------------------------------------
# Step 10: Print a few confidence examples
# ----------------------------------------------------------------------------------------

# Confidence here means the model's highest score for its predicted class.
# It is useful information, but it is not a guarantee that the model is correct.
print("\n--- Example predictions ---")

for index in range(3):
    predicted_label_index = np.argmax(predictions[index])
    predicted_label = fashion_mnist_class_names[predicted_label_index]
    true_label = fashion_mnist_class_names[test_labels[index]]
    confidence = predictions[index][predicted_label_index]

    print(
        f"Example {index + 1}: predicted '{predicted_label}' "
        f"with confidence {confidence:.3f} | true label: '{true_label}'"
    )

print("\n--- Saved files ---")
print("outputs/fashion_mnist_training_accuracy.png")
print("outputs/fashion_mnist_prediction_examples.png")
