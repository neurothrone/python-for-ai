"""
Explore the Fashion MNIST dataset

This script is the first Week 7 lecture demo.
It does not train a neural network yet.

The goal is to understand the data before modeling:
- Load Fashion MNIST.
- Inspect the shape of the data.
- Connect numeric labels to readable class names.
- Show a small grid of example images.

This is the same habit as earlier weeks: look at the data before choosing or
training a model.
"""

import os
from pathlib import Path

import matplotlib.pyplot as plt

# Reduce TensorFlow system messages so the output stays easier to read.
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")

from utils import fashion_mnist_class_names, load_fashion_mnist

# ----------------------------------------------------------------------------------------
# Path handling: reliably locate files relative to this script
# ----------------------------------------------------------------------------------------

# The script lives in the lecture folder.
# Keeping outputs beside the lecture scripts makes the folder easier to move or share.
BASE_DIR = Path(__file__).resolve().parent
OUTPUTS_DIR = BASE_DIR / "outputs"

# Create the outputs folder if it does not already exist.
OUTPUTS_DIR.mkdir(exist_ok=True)

# ----------------------------------------------------------------------------------------
# Step 1: Load the dataset
# ----------------------------------------------------------------------------------------

# Fashion MNIST is included with Keras, which is part of TensorFlow.
# It contains 70,000 labeled grayscale clothing images:
# - 60,000 images for training.
# - 10,000 images for testing.
# - Each image is 28 x 28 pixels.
# This makes it useful for a first neural-network demo because the data is already
# prepared, labeled, and large enough to train a small model.
(train_images, train_labels), (test_images, test_labels) = load_fashion_mnist()

# ----------------------------------------------------------------------------------------
# Step 2: Connect numeric labels to readable class names
# ----------------------------------------------------------------------------------------

# The dataset labels are numbers from 0 to 9.
# The model works with the numbers, but humans read the class names more easily.
# `fashion_mnist_class_names` comes from the dataset, through utils.py.
# We are not inventing our own categories here.

# ----------------------------------------------------------------------------------------
# Step 3: Inspect the dataset
# ----------------------------------------------------------------------------------------

print("--- Dataset shapes ---")
print("Training images:", train_images.shape)
print("Training labels:", train_labels.shape)
print("Test images:", test_images.shape)
print("Test labels:", test_labels.shape)

print("\n--- Image values ---")
print("Smallest pixel value:", train_images.min())
print("Largest pixel value:", train_images.max())

print("\n--- First training label ---")
first_label = train_labels[0]
print("Numeric label:", first_label)
print("Class name:", fashion_mnist_class_names[first_label])

# ----------------------------------------------------------------------------------------
# Step 4: Visualize the first 18 training images
# ----------------------------------------------------------------------------------------

# This shows the first 18 images in the training data, in their original order.
# It is not trying to show one example of every class.
# That is why we may see repeated categories, such as two sandals or two T-shirts.
# The goal is simply to connect the image arrays with human-readable labels.
number_of_images_to_show = 18

print("\n--- Image grid ---")
print(f"Showing the first {number_of_images_to_show} training images, not one image per class.")

# We use a 3 x 6 grid because it fits 18 images neatly.
# `axes.flat` lets us loop through all small plot areas in the grid.
fig, axes = plt.subplots(3, 6, figsize=(15, 8))
fig.suptitle(f"First {number_of_images_to_show} Training Images", fontsize=14)

for index, ax in enumerate(axes.flat[:number_of_images_to_show]):
    # `imshow` displays a 2D array as an image.
    # `cmap=plt.cm.binary` shows the grayscale image in black and white.
    ax.imshow(train_images[index], cmap=plt.cm.binary)

    label_index = train_labels[index]
    ax.set_title(fashion_mnist_class_names[label_index], fontsize=10)

    # The axes are not helpful for these small clothing images, so we hide them.
    ax.axis("off")

# `tight_layout` tries to space the small plots nicely.
# `rect=(0, 0, 1, 0.95)` keeps the layout inside the lower 95% of the figure.
# That leaves a little room at the top for the main title.
plt.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig(OUTPUTS_DIR / "fashion_mnist_sample_images.png")
plt.show()
plt.close(fig)

print("\n--- Saved files ---")
print("outputs/fashion_mnist_sample_images.png")
