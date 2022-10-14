from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle
import os

PATH = os.path.dirname(__file__)

data = load_iris()
X = pd.DataFrame(data=data.data, columns=data.feature_names)
target_to_labels = {k: v for k, v in zip([0, 1, 2], data['target_names'])}
y = [target_to_labels.get(k) for k in data['target']]

model = RandomForestClassifier()
model.fit(X, y)

with open(f'{PATH}/model.pickle', 'wb') as handle:
    pickle.dump(model, handle, protocol=pickle.HIGHEST_PROTOCOL)
