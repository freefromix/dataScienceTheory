# Shallow neural networks summary with algo

## Algorithm

```
# train
for i in 10000:{

  Z1,A1,Z2,A2=forward_propagation(X,W1,b1,W2,b2){W1X+b1, tanh(), W2A1+b2, sigmoid()}

  cost=compute_cost(Y,A2){see below 1}

  dW1,db1,dW2,db2=backward_propagation(X,Y,W1,W2,A1,A2){See below 2}

  W1,b1,W2,b2=update_parameters(update_rate,W1,b1,W2,b2,dW1,db1,dW2,db2){}

}


# predict
A2, cache = forward_propagation(X, parameters)
predictions = np.round(A2)

mean_prediction = np.mean(predictions)
accuracy = float((np.dot(Y,predictions.T) + np.dot(1-Y,1-predictions.T))/float(Y.size)*100)

```

```
Cost after iteration 0: 0.693048
Cost after iteration 1000: 0.288083
Cost after iteration 2000: 0.254385
Cost after iteration 3000: 0.233864
Cost after iteration 4000: 0.226792
Cost after iteration 5000: 0.222644
Cost after iteration 6000: 0.219731
Cost after iteration 7000: 0.217504
Cost after iteration 8000: 0.219471
Cost after iteration 9000: 0.218612
```
```
Accuracy for 1 hidden units: 67.5 %
Accuracy for 2 hidden units: 67.25 %
Accuracy for 3 hidden units: 90.75 %
Accuracy for 4 hidden units: 90.5 %
Accuracy for 5 hidden units: 91.25 %
Accuracy for 20 hidden units: 90.0 %
Accuracy for 50 hidden units: 90.25 %
```

## Explanations

----

See below 1:

<img src="../img/cost.png" width="400" />

```python
logprobs = np.multiply(np.log(A2), Y) + np.multiply((1 - Y), np.log(1 - A2))
cost = -np.sum(logprobs)/m
```

----

See below 2:

<img src="../img/summary_of_gradient_descent.png" width="400" />


```python
dZ2 = A2-Y
dW2 = np.dot(dZ2,A1.T)/m
db2 = np.sum(dZ2,axis=1,keepdims=True)/m
dZ1 = np.dot(W2.T,dZ2)*(1 - np.power(A1, 2))
dW1 = np.dot(dZ1, X.T)/m
db1 = np.sum(dZ1,axis=1,keepdims=True)/m
```