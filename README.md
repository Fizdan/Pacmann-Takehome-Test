# Pacmann-Takehome-Test

## Problem: KNN Regression

### Installation
------------

Put script **knnRegression.py** in the same folder as the main script, or in subfolder with modified path in import

### Usage
------------

```py
from knnRegression import KnnRegression
regressor = KnnRegression(n_neighbors = 10)
```

### Example
------------

```py
knn = KnnRegression(n_neighbors = n_neighbors, metrics="Euclidean")
y_pred = knn.fit(X_train, y_train).predict(X_test)

plt.scatter(X_train, y_train, color='darkorange', label='data')
plt.plot(X_test, y_pred, color='navy', label='prediction')

plt.legend()
plt.title("K Nearest Neighbors Regressor")

plt.show()
```

### Params
------------

Parameter that the module used

| Params      | Type   | Description                                                                 |
|-------------|--------|-----------------------------------------------------------------------------|
| n_neigbours | int    | Number of neigbours used i.e (1,5,20)                                       |
| methods     | string | Methods used in distance metrics in {"Euclidean", "Manhattan", "Minkowski"} |

### Methods
------------

- Euclidan Distance
  
    source:

- Manhattan Distance
  
    source:

- Minkowski Distance

    source: