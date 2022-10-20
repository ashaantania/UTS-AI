#Asha Antania Anjani
#21091397068 - B

import numpy as np

# Layer input 10 features
inputs = [1.0, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 4.5, 5.5, 5.5]
weights = [0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.5]

# Neuron 1
bias = 4.5

outputs = np.dot(weights, inputs) + bias
print(outputs)
