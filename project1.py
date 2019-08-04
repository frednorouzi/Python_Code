"""
Fariborz Norouzi
MET_CS521
6/18/2018
Term Project _ part1
Description:
 This mini project is getting Machin Learning approach in Python by reading 
 one-year historical data of the ticker 'GE' as a sample data and fit to linear
 and Radial Basis Functions (RBF) regression models for predicting future
 values. It is a popular kernel function which used in support vector machine
 classification.
  """ 
import time
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR

# Create empty list
prices = []
dates = []

def prediction_prices(dates, prices, x):
    ''' Method for predicting future prices by trained models where it uses 
        linear and rbf regression models.
    '''
    # A numpy reshapes into a vector using reshape function with parameter
    dates = np.reshape(dates,(len(dates),1))
    # Support Vector Regression (SVR) using linear kernels
    svr_lin = SVR(kernel = 'linear', C=1e3)
    # Support Vector Regression (SVR) using non-linear kernels
    svr_rbf = SVR(kernel = 'rbf', C=1e3, gamma = 0.1)
    # Calculate time processing for linear regression model
    start_time = time.time()
    # fit a linear regression model to the underlying data set
    svr_lin.fit(dates,prices)
    # Display time of complete processing for linear kernels 
    print("Linear Fit Complete in {0:.4f} seconds."
          .format(time.time() - start_time))
    print()
  

    
    # Calculate time processing for non-linear regression model
    start_time = time.time()
    # fit a non-linear regression model to the underlying data set
    svr_rbf.fit(dates,prices)
    # Display time of complete processing for non-linear kernels 
    print("RBF Fit Complete in {0:.4f} seconds"\
          .format(time.time() - start_time))
    print()
    # Making variable for fitting a linear regression
    linear_prediction = svr_lin.predict(x)[0]
    # Making variable for fitting a non-linear regression
    rbf_prediction = svr_rbf.predict(x)[0] 
    
    
    # Display prediction results
    print("Linear Prediction is: {0:.4f}".format(linear_prediction))
    print("=======================================")
    print("RBF Prediction is: {0:.4f}".format(rbf_prediction))
   
    plt.scatter(dates,prices,color='black', label='Data')
    
    plt.plot(dates,svr_rbf.predict(dates), color = 'red', label = 'RBF model')
    
    plt.plot(dates,svr_lin.predict(dates), color = 'blue',
            label = 'Linear model')

	# Plot data
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()
    
    return rbf_prediction, linear_prediction

# Test program    
def main():
    # Check user input
    while True:
        try:
            # User input
            filename = input('Enter a filename: ').strip()
            # Open file
            csvFile = open(filename, 'r')
            break
        except IOError:
            print('File ' + filename + ' does not exist. Try again.')
    # read file            
    csvFileReader = csv.reader(csvFile)
    # Calculate time processing for reading data
    start_time = time.time()
    next(csvFileReader)
    # Generate dates and prices lists
    for row in csvFileReader:
        dates.append(int(row[0].split('-')[0]))
        prices.append(float(row[1]))
    
    # Display time of complete processing for reading file 
    print("Completed reading file : {0:} in {1:.5f} seconds."
           .format(filename,time.time() - start_time))
    print()
    print(prices)
    print()          
    prediction_prices(dates,prices,31)


# run test program
if __name__ == '__main__':
    main()





