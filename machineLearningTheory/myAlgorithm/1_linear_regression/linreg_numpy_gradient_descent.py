import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

my_data = pd.read_csv('data/home.csv',names=["size","bedroom","price"])

#we need to normalize the features using mean normalization
my_data = (my_data - my_data.mean())/my_data.std()


#setting the matrixes
X = my_data.iloc[:,0:2]
ones = np.ones([X.shape[0],1])
X = np.concatenate((ones,X),axis=1)

y = my_data.iloc[:,2:3].values #.values converts it from pandas.core.frame.DataFrame to numpy.ndarray
theta = np.zeros([1,3])

#computecost
def computeCost(X,y,theta):
    tobesummed = np.power(((X @ theta.T)-y),2)
    return np.sum(tobesummed)/(2 * len(X))

def gradientDescent(X,y,theta,iters,alpha):
    cost = np.zeros(iters)
    m = len(X)
    for i in range(iters):
        theta = theta - (alpha/m) * np.sum((X @ theta.T - y)*X, axis=0)
        print("(X @ theta.T - y).shape: ", (X @ theta.T - y).shape)
        print("((X @ theta.T - y)*X).shape: ",((X @ theta.T - y)*X).shape)
        print("(X @ theta.T - y)*X, axis=0).shape", np.sum((X @ theta.T - y)*X, axis=0).shape)
        print("----------------------------------------------")
        cost[i] = computeCost(X, y, theta)
    
    return theta,cost

#set hyper parameters
alpha = 0.01
iters = 10000

thetas,cost = gradientDescent(X,y,theta,iters,alpha)
print(thetas)

finalCost = computeCost(X,y,thetas)
print("finalCost:", finalCost)

fig, ax = plt.subplots()
ax.plot(np.arange(iters), cost, 'r')  
ax.set_xlabel('Iterations')  
ax.set_ylabel('Cost')  
ax.set_title('Error vs. Training Epoch')


'''
# scikit.learn results
theta0: -0.9268523297987521e-16
theta1: 0.8847659878549523
theta2: -0.05317881966327953

scikit.learn use 1/m not 1/2m
finalCost: 0.26137296107808383
'''
print(theta.shape)