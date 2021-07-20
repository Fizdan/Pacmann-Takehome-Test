# Pacmann Takehome Test

## Problem: KNN Regression

### Installation
------------

Clone the repo , then run:

```bash
pip install requirement.txt
```

### Usage
------------

```py
from knnRegression import KnnRegression
regressor = KnnRegression(n_neighbors = 10, metrics="Euclidean")
```

### Example
------------

```py
# Instantiate Regressor, Default 5 Neighbour and used Euclidean Metrics
knn = KnnRegression()

# Fit train data and label data into regressor
knn.fit(X_train, y_train)

# Predict the inserted input
y_pred = knn.predict(X_test)
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
  
    The manhattan distance between two points is defined as:


    $$ d\left( p,q\right)   = \sqrt {\sum _{i=1}^{n}  \left( q_{i}-p_{i}\right)^2 } $$

    The Euclidean distance is a distance measure between two points or or vectors in a two- or multidimensional (Euclidean) space based on Pythagoras' theorem. The distance is calculated by taking the square root of the sum of the squared pair-wise distances of every dimension.

- Manhattan Distance

    The manhattan distance between two points is defined as:


    $$ d\left( x,y\right)   = \sum _{i=1}^{n}  |x_{i}-y_{i}|  $$
  
    The Manhattan distance (sometimes also called Taxicab distance) metric is related to the Euclidean distance, but instead of calculating the shortest diagonal path ("beeline") between two points, it calculates the distance based on gridlines. The Manhattan distance was named after the block-like layout of the streets in Manhattan.

- Minkowski Distance

    $$  d\left( x,y\right)   = \left(\sum_{i=1}^n |x_i-y_i|^p\right)^{1/p}  $$

    The Minkowski distance is a generalized form of the Euclidean distance and the Manhattan distance .

Source : [Equation and Definition](https://github.com/rasbt/pattern_classification/blob/master/resources/latex_equations.md)
