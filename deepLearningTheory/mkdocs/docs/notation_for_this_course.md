  * Y Output (for example wage).
  * $\hat{f}$: represents our estimate for f.
  * $\hat{Y}$ represents the resulting prediction for Y.

----


  * *n* to represent the number of distinct data points, or observations, in our sample (for example 3,000 people).
  * *p* denote the number of variables that are available for use in making predictions (such as year, age, and more).
  * $X_{ij}$ input with:
    * *i* = 1, 2,...,*n*
    * *j* = 1, 2,...,*p*
  * *j*th variable for the *i*th observation

$$X_{ij} = 
 \begin{pmatrix}
  x_{11} & x_{12} & \cdots & x_{1p} \\
  x_{21} & x_{22} & \cdots & x_{2p} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  x_{n1} & x_{n2} & \cdots & x_{np} 
 \end{pmatrix}$$


----


  * Rows of X: At times we will be interested in the rows of X, which we write as x1, x2,...,xn. Here $X_{i}$ is a vector of length p, containing the p variable measurements for the *i*th observation. That is:

$$X_{i} = 
 \begin{pmatrix}
  x_{i1} \\
  x_{i2} \\
  \vdots  \\
  x_{ip} 
 \end{pmatrix}$$

  * Columns of X (Vectors are by default represented as columns): At other times we will be interested in the columns of X which we write as x1, x2,..., xp. Each is a vector of
length n. 

----

$(x_{0}, y_{0})$ is a previously unseen test observation not used to train the statistical learning method.

----

$$X_{j} = 
 \begin{pmatrix}
  x_{1j} \\
  x_{2j} \\
  \vdots  \\
  x_{nj} 
 \end{pmatrix}$$

For example, for the Wage data, x1 contains the n = 3,000 values for year. Using this notation, the matrix X can be written as:

$X =  \begin{pmatrix}x_{1} & x_{2} & \cdots & x_{p}\end{pmatrix}$

OR

$$X^T = 
 \begin{pmatrix}
  x_{1}^T \\
  x_{2}^T \\
  \vdots  \\
  x_{n}^T 
 \end{pmatrix}$$

----

  * The $^T$ notation denotes the transpose of a matrix or vector. So, for example:

$$X^T = 
 \begin{pmatrix}
  x_{11} & x_{12} & \cdots & x_{n1} \\
  x_{12} & x_{22} & \cdots & x_{n2} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  x_{1p} & x_{2p} & \cdots & x_{np} 
 \end{pmatrix}$$

while:

$$X_{i}^T = 
 \begin{pmatrix}
  x_{i1} & x_{i2} & \cdots & x_{ip} 
 \end{pmatrix}$$


----

$y_{i}$: We use $y_{i}$ to denote the ith observation of the variable on which we wish to make predictions, such as wage. Hence, we write the set of all n observations in vector form as:

$$y = 
 \begin{pmatrix}
  y_{1} \\
  y_{2} \\
  \vdots  \\
  y_{n} 
 \end{pmatrix}$$


$\sum{(y - \hat{y})²}=\sum{[f(x)+\epsilon-\hat{f}(x)]²}$

