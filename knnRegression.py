# Imports
import numpy as np

# Class
class KnnRegression() :

    """
    **Implementation**

    Method:

    - fit(X_train, y_train):
        Fits model to training data

    - predict(X):
        Returns predictions for X based on fitted model

    """

    # Initialization
    def __init__(self, n_neighbors = 5, metrics='Euclidean'):
    
        """
        Initialization for Algorithm

        Inputs      : learning_rate : list or array contains int or float 
                      epochs : list or array contains int or float 
                      metrics : string - {'Euclidean', 'Manhattan', 'Minkowski'} 

        Output      : N/A pass along to predict()
        """

        self.n_neighbors = n_neighbors
        self.metrics = metrics

    def fit( self, X, Y) :

        """
        Fits model to training data, calculate cost, and return weight and bias

        Inputs      : x : list or array contains int or float, training Data
                      Y : list or array contains int or float, training Label

        Output      : N/A pass along to predict()
        """

        self.train_data = X
        self.label_data = Y

        return self

    def predict( self, X ) :

        """
        Returns list of mean of K nearest neighbors

        Inputs      : X : list or array contains int or float

        Output      : Y_predict: list or array contains float

        Reference   : http://www.saedsayad.com/k_nearest_neighbors_reg.html
        """
                
        Y_predict = np.zeros( X.shape[0] )
          
        for i in range( X.shape[0] ) :
              
            x_index = X[i]
                            
            neighbors = np.zeros( self.n_neighbors )
              
            neighbors = self.__nearest_neighbors( x_index )
                            
            Y_predict[i] = np.mean( neighbors )
              
        return Y_predict


        

    def __nearest_neighbors( self, x ) :      

        """
        Returns sorted distances limited by neighbour count

        Inputs      : X : list or array contains int or float

        Output      : label_sorted: list or array contains float

        Reference   : http://www.saedsayad.com/k_nearest_neighbors_reg.htm
        """    
          
        distancesList = np.zeros( self.train_data.shape[0] )
          
        for i in range( self.train_data.shape[0] ) :
        
            if self.metrics == 'Euclidean':

                distance = self.__euclidean( x, self.train_data[i] )
                
                distancesList[i] = distance

            elif self.metrics == 'Manhattan':

                distance = self.__manhattan( x, self.train_data[i] )
                
                distancesList[i] = distance

            elif self.metrics == 'Minkowski':

                distance = self.__minkowski( x, self.train_data[i] )
                
                distancesList[i] = distance

            else :

                raise ValueError("Invalid Distance metrics for KNN Regression") 

        # Sort the distances and get label by neighbour count

        sortIndex = distancesList.argsort()
          
        label_sorted = self.label_data[sortIndex]
          
        return label_sorted[:self.n_neighbors]

              
    def __euclidean( self, x, x_train ) :

        """
        Returns euclidian distance of values between x and x_train

        Inputs      : X : list or array contains int or float

        Output      : list or array contains float

        Reference   : https://en.wikipedia.org/wiki/Euclidean_distance
        """  
          
        return np.sqrt( np.sum( np.square( x - x_train ) ) )

              
    def __manhattan( self, x, x_train ) :

        """
        Returns manhattan distance of values between x and x_train

        Inputs      : X : list or array contains int or float

        Output      : list or array contains float

        Reference   : http://www.improvedoutcomes.com/docs/WebSiteDocs/Clustering/Clustering_Parameters/Manhattan_Distance_Metric.html
        """  
          
        return np.sum(np.abs(x-x_train))

              
    def __minkowski( self, x, x_train ) :

        """
        Returns minkowski distance of values between x and x_train

        Inputs      : X : list or array contains int or float

        Output      : list or array contains float

        Reference   : https://rittikghosh.com/Minkowski_distance.html
        """  
          
        return np.sum(np.abs(x - x_train)**len(x))**(1/len(x))
    