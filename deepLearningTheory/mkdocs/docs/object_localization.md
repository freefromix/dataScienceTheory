# Object localization

<img src="../img/screenshot_from_2019-02-16_18-34-50.png" width="400" />

## Classification with localization

<img src="../img/screenshot_from_2019-02-16_18-54-14.png" width="400" />

$$\begin{bmatrix}
p_{c} \\
b_{x} \\
b_{y} \\
b_{h} \\
b_{w} \\
c_{1} \\
c_{2} \\
c_{3} \\
\end{bmatrix}=\begin{bmatrix}
is\ there\ an\ object? \\
x\ bounding\ box\ for\ the\ object \\
y\ bounding\ box\ for\ the\ object \\
height\ bounding\ box\ for\ the\ object \\
width\ bounding\ box\ for\ the\ object \\
pedestrian \\
car \\
motorcycle \\
\end{bmatrix}$$

- Pc = is there an object?
- bx,by,bh,bw: bounding box for the object
- c1, c2, c3, c4 respectivly: pedestrian, car, motorcycle, background (neither).


## Loss

__**If you are using squared error:**__

| Case | Loss formula |
|------|--------------|
| There is an object ($y_{1}=1$) | $\mathcal{l}(\hat{y},y)=(\hat{y_{1}}-y_{1})^2+(\hat{y_{2}}-y_{2})^2+ ... +(\hat{y_{8}}-y_{8})^2$ |
| There is no object ($y_{1}=0$) | $\mathcal{l}(\hat{y},y)=(\hat{y_{1}}-y_{1})^2$ | 