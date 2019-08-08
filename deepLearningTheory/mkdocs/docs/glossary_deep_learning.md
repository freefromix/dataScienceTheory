# Glossary Deep Learning

**Gradient**: Slope of a function but multi-dimensional. The gradient of a function gives you the direction of steepest ascent (which direction should you step to increase the function most quickly). Naturally taking the negative of the gradient gives you the direction of steepest descent (which direction should you step to decrease the function most quickly).

**Unstructured data**: Unstructured data represents any data that does not have a recognizable structure. It is unorganized and raw and can be non-textual or textual. For example, email is a fine illustration of unstructured textual data. It includes time, date, recipient and sender details and subject, etc., but an email body remains unstructured. In customer-centered businesses, the data found in an unstructured form may be examined to enhance relationship marketing and customer relationship management (CRM). As social media apps, such as Facebook and Twitter, go mainstream, unstructured data development is likely to outrun the progress of structured data.

**Transposition**: $w^{T}$ is the Transposition of the matrix w.

**Simple linear regression**: 1 dependent variable (interval or ratio), 1 independent variable (interval or ratio or dichotomous)
 
**Multiple linear regression**: 1 dependent variable (interval or ratio) , 2+ independent variables (interval or ratio or dichotomous)
 
**Logistic regression**: 1 dependent variable (dichotomous), 2+ independent variable(s) (interval or ratio or dichotomous). Logistic regression is a learning algorithm used in a supervised learning problem when the output y are all either 0 or 1.
 
**Ordinal regression**: 1 dependent variable (ordinal), 1+ independent variable(s) (nominal or dichotomous)

**Multinominal regression**: 1 dependent variable (nominal), 1+ independent variable(s) (interval or ratio or dichotomous)

**Loss function**: The loss function measures how well you're doing on a single training example.

**Cost function**: The cost function measures how well your parameters w and b are doing on your entire training set.

**Gradient descent**: Gradient descent is a first-order iterative optimization algorithm for finding the minimum of a function. To find a local minimum of a function using gradient descent, one takes steps proportional to the negative of the gradient (or approximate gradient) of the function at the current point.

**Inner product of 2 vectors**: It  produces a scalar. 

$$w^{T}x = \begin{bmatrix}
  w_{1} & w_{2} & w_{3} & \cdots & w_{n_{x}} 
 \end{bmatrix} \begin{bmatrix}
  x_{1} \\
  x_{2} \\
  x_{3} \\
  \cdots  \\
  x_{n_{x}} 
 \end{bmatrix} = w_{1}x_{1}+w_{2}x_{2}+w_{3}x_{3}+...+w_{n_{x}}x_{n_{x}}$$

**Outer product of 2 vectors**: It  produces a matrix.

$$\begin{bmatrix}
  y_{1} \\
  y_{2} \\
  y_{3} \\
  \cdots  \\
  y_{n_{x}}
 \end{bmatrix} \begin{bmatrix}
  x_{1} & x_{2} & x_{3} & \cdots & x_{n_{x}} 
 \end{bmatrix} = \begin{bmatrix}
  x_{1}y_{1} & x_{1}y_{2} & x_{1}y_{3} & \cdots & x_{1}y_{n_{x}}\\
  x_{2}y_{1} & x_{2}y_{2} & x_{2}y_{3} & \cdots & x_{2}y_{n_{x}}\\
  x_{3}y_{1} & x_{3}y_{2} & x_{3}y_{3} & \cdots & x_{3}y_{n_{x}}\\
  \cdots  \\
  x_{n_{x}}y_{1} & x_{n_{x}}y_{2} & x_{n_{x}}y_{3} & \cdots & x_{n_{x}}y_{n_{x}}
 \end{bmatrix}$$

**Dot product of 2 matrices**: It  produces a matrix.

$$\begin{bmatrix}
  a & b \\
  c & d \\
 \end{bmatrix} . \begin{bmatrix}
  w & x \\
  y & z \\
 \end{bmatrix}=\begin{bmatrix}
  aw+by & ax+bz \\
  cw+dy & cx+dz \\
 \end{bmatrix}$$

**Neural Network**: A neural network can model any function (not just linear functions). A Neural Network has got non linear activation layers which is what gives the Neural Network a non linear element. So a NN can predict non-linear functions.

**Euclidian distance**: $\left\lVert u \right\rVert$ = length of the vector u. For a simple vector you can use pythagore.

**Linear Polynomials**: After combining the degrees of terms if the highest degree is 1 it is called Linear Polynomials 

- example 1: 2x
- example 2: 2x+2
- example 3: 2x+2y+3

**Quadratic Polynomials**: After combining the degrees of terms if the highest degree of any term is 2 it is called Quadratic Polynomials.

- example 1: $2x^{2}$
- example 2: $2x^{2}+2y+2$
- example 3: $2xy+2y$
  - This can also be written as $2x^1y^1 + 2y^1$ 
  After combining the degrees of term 2xy the sum total of degree is 2. So it is a Quadratic Polynomial.

**Cubic Polynomials**: After combining the degrees of terms if the highest degree of any term is 3 it is called Cubic Polynomials.

- example 1: $2x^{3} + 2y2 + 2$ 
- example 2: $2x^{2}z + 2y$
  - This can also be written as $2x^{2}z^{1} + 2y^{1}$.
  - After combining the degrees of term $2x^{2}z^{1}$, the sum total of degree is 3
  - Term $2y^{1}$ has degree 1. 
- example 3: $2xyz + 2y + 2$
  - $2x^1y^1z^1 + 2y^1 + 2$
  - After combining the degrees of term $2x^1y^1z^1$, the sum total of degree is 3
  - Term $2y^{1}$ has degree 1. 
- example 4: $2x^{2}y + 2y + 2$

**Forward propagation**: In neural networks, you forward propagate to get the output and compare it with the real value to get the error.

**Backward propagation**: Now, to minimize the error, you propagate backwards by finding the derivative of error with respect to each weight and then subtracting this value from the weight value.