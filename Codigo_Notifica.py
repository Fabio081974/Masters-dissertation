import numpy as np
import pandas as pd

# Carrega data traffic dataset
data = pd.read_csv('data_traffic.csv')

# Calcula (mean and standard deviation)
mean = np.mean(data)
std = np.std(data)

# Define (threshold for anomalies)
threshold = 3 * std

# Checa anomalias
anomalies = []
for i in range(len(data)):
    z_score = (data[i] - mean) / std
    if np.abs(z_score) > threshold:
        anomalies.append(i)

print("Anomalias encontrada para Ativo X: ", anomalies)
