# Principal Component Analysis (PCA)

## PCA Problem Formation
- Let's say we have the following 2D data
![](img/unsupervisedlearning20.png)
    1. We can project with a diagonal line (red line)
        - PCA reduces the blue lines (the projection error)
            - Before performing PCA, perform mean normalization (mean = 0) and feature scaling
    2. We can also project with another diagonal line (magenta)
        - But the projection errors are much larger
        - Hence PCA would choose the red line instead of this magenta line
- Goal of PCA
    - It's trying to find a lower dimensional surface onto which to project the data, so as to minimize this squared projection error
    - To minimize the square distance between each point and the location of where it gets projected. 
    ![](img/unsupervisedlearning21.png)
- PCA is not linear regression
    - PCA is a minimization of the orthogonal distance
    ![](img/unsupervisedlearning22.png)

## 2b. Principal Component Analysis Algorithm

Data pre-processing step
  - You must always do this before doing PCA
  ![](img/unsupervisedlearning23.png)
    - $S_j$ could be: $S_j=Max-Min$

<br>

- PCA intuition
    - You need to compute the vector or vectors
        ![](img/unsupervisedlearning24.png)
        - Left graph: compute vector $z_1$
        - Right graph: compute vector $z_1$ and $z_2$

### PCA Algorithm

Reduce data from n-dimensions to k-dimensions

----

Compute "covariance matrix" $\Sigma$ (sigma)

$\Sigma = \frac{1}{m} \displaystyle \sum_{i=1}^{n} (x^{(i)})(x^{(i)})^T$
Compute "eigenvectors" of matrix $\Sigma$:
  [U,S,V] = svd(Sigma)

----

![](img/unsupervisedlearning25.png)

- You can use eig (eigen) or svd (singular value decomposition) but the svd is more stable.
  - You can use any library in other languages that does singular value decomposition
  - You will get 3 matrices: U, S and V
  - But we only need matrix U where we manipulate to get z that is a k x 1 vector

![](img/unsupervisedlearning26.png)

## Applying PCA

### Reconstruction from Compressed Representation
- We can go from lower dimensionality to higher dimensionality
![](img/unsupervisedlearning28.png)

### Choosing the Number of Principal Components
- k is the number of principal components 
    - But how do we choose k?
    ![](img/unsupervisedlearning29.png)
- There is a more efficient method on the right compared to the left
    - We then use the S matrix for calculations 
    ![](img/unsupervisedlearning30.png)
    ![](img/unsupervisedlearning31.png)
- You would realise that PCA can retain a high percentage of the variance even after compressing the number of dimensions of the data

### Advice for Applying PCA
- Supervised learning
    - For many data sets, we can reduce by 5-10x easily to ensure our learning algorithm runs much faster
    ![](img/unsupervisedlearning32.png)
- Application of PCA
    1. Compression
        - Reduce memory or disk needed to store data
        - Speed up learning algorithm   
            - We choose k by percentage of variance retained
    2. Visualization
        - We choose only k = 2 or k = 3 
- Bad uses of PCA
    1. To prevent over-fitting
        - Regularization is better because it is less likely to throw away valuable information as it knows the labels
        ![](img/unsupervisedlearning33.png)
    2. Running PCA without consideration
        ![](img/unsupervisedlearning34.png)