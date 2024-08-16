import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math






def softmax(x):
  """It takes a vector of real numbers as input and outputs a probability distribution over multiple classes."""
  e_x = np.exp(x - np.max(x))
  return e_x / np.sum(e_x, axis=0)

class_labels = ["Class A", "Class B", "Class C"]
probabilities = np.array([0.2, 0.3, 0.5])
plt.bar(class_labels, probabilities)
plt.xlabel("Classes")
plt.ylabel("Probability")
plt.title("Softmax Activation Function")








def plot_softmax():
    class_labels = ["Class A", "Class B", "Class C"]
    probabilities = np.array([0.2, 0.3, 0.5])
    plt.bar(class_labels, probabilities)
    plt.xlabel("Classes")
    plt.ylabel("Probability")
    plt.title("Softmax Activation Function")
    plt.show()



