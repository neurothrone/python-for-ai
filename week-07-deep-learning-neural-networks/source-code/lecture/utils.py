"""
Shared helper functions for the Week 7 lecture demos.

Keeping shared code here prevents us from repeating the same dataset-loading
logic in every demo script.
"""

import gzip
from pathlib import Path

import numpy as np
import tensorflow as tf

# Readable class names for Fashion MNIST labels.
# The labels in the dataset are numbers from 0 to 9.
fashion_mnist_class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]


def load_fashion_mnist():
    """Load Fashion MNIST from the local cache if possible, otherwise from Keras."""

    # Keras can download this dataset automatically.
    # In this local lecture folder, we first check the cache to avoid network issues.
    local_dataset_dir = Path.home() / ".keras" / "datasets" / "fashion-mnist"

    required_files = {
        "train_labels": local_dataset_dir / "train-labels-idx1-ubyte.gz",
        "train_images": local_dataset_dir / "train-images-idx3-ubyte.gz",
        "test_labels": local_dataset_dir / "t10k-labels-idx1-ubyte.gz",
        "test_images": local_dataset_dir / "t10k-images-idx3-ubyte.gz",
    }

    if not all(path.exists() for path in required_files.values()):
        print("--- Dataset source ---")
        print("Loading Fashion MNIST through Keras.")
        return tf.keras.datasets.fashion_mnist.load_data()

    with gzip.open(required_files["train_labels"], "rb") as file:
        local_train_labels = np.frombuffer(file.read(), np.uint8, offset=8)

    with gzip.open(required_files["train_images"], "rb") as file:
        local_train_images = np.frombuffer(file.read(), np.uint8, offset=16).reshape(
            len(local_train_labels), 28, 28
        )

    with gzip.open(required_files["test_labels"], "rb") as file:
        local_test_labels = np.frombuffer(file.read(), np.uint8, offset=8)

    with gzip.open(required_files["test_images"], "rb") as file:
        local_test_images = np.frombuffer(file.read(), np.uint8, offset=16).reshape(
            len(local_test_labels), 28, 28
        )

    print("--- Dataset source ---")
    print("Loaded Fashion MNIST from the local Keras cache.")

    return (local_train_images, local_train_labels), (
        local_test_images,
        local_test_labels,
    )
