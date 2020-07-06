# Alexandros Metsai
# alexmetsai@gmail.com

from data_loader import load_data
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
import pickle

# Set random seed for reproduction
np.random.seed(1)

# Load data from csv.
dataset = load_data()

# Randomly separate data 80/20.
dataset_size = len(dataset)
randIdx = np.arange(dataset_size)
np.random.shuffle(randIdx)
N_train = int(dataset_size * 0.8)

train_data = dataset[randIdx[:N_train]]
test_data = dataset[randIdx[N_train:]]

# Use K-means to find clusters for normal and anomalous data.
kmeans = KMeans(n_clusters=2) 
kmeans.fit(train_data[:,:-1]) 

# Calculte training and testing accuracy.
train_pred = kmeans.predict(train_data[:,:-1])
test_pred = kmeans.predict(test_data[:,:-1])

train_acc = accuracy_score(train_data[:,-1], train_pred)
test_acc = accuracy_score(test_data[:,-1], test_pred)

print("Training accuracy:", train_acc)
print("Testing accuracy:", test_acc)

# Save model for inference.
pickle.dump(kmeans, open("model.pk", 'wb'))
