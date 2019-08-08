# RMSprop root mean square prop

## Algorithm

On iteration t:
{

dW,db = Compute dW,db on current mini-batch


$S_{dW}=\beta S_{dW} + (1-\beta)dW^2$

$S_{db}=\beta S_{db} + (1-\beta)db^2$

$W=W-\alpha\frac{dW}{\sqrt{S_{dW}}}$

$b=b-\alpha\frac{db}{\sqrt{S_{db}}}$

}

<img src="../img/warning.png" width="20" />$dW^2$ Square is element-wise.

|           |               |
|-----------|---------------|
| $\alpha$  | Learning rate |
| $\beta$   | Control the exponentially weighted average. The most common value for $\beta$ is 0.9 (last 10 iteration's gradient) |

## Explanation

<img src="../img/screenshot_from_2019-01-03_14-59-30.png" width="400" />
<img src="../img/untitled_diagram.png" width="400" />

And indeed if you look at the derivatives, these derivatives are much larger in the vertical direction than in the horizontal direction. So the slope is very large in the b direction, right? So with derivatives like this, this is a very large db and a relatively small dw. Because the function is sloped much more steeply in the vertical direction than as in the b direction, than in the w direction, than in horizontal direction.

So the net effect of this is that your up days in the vertical direction are divided by a much larger number, and so that helps damp out the oscillations. Whereas the updates in the horizontal direction are divided by a smaller number. So the net impact of using RMSprop is that your updates will end up looking more like this. (green)

<img src="../img/screenshot_from_2019-01-03_15-01-28.png" width="400" />