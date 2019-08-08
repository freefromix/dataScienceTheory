# Satisficing and Optimizing metric

| Classifier  | Accuracy  | Running time  |
|-------------|-----------|---------------|
| A           | 90%       | 80 ms     |
| B           | 92%       | 95 ms     |
| C           | 95%       | 1500 ms   |


You want to do as well as possible on accuracy which is more important. Running time is what we call a satisficing metric (it just has to be good enough). It just needs to be less than 100 milliseconds and beyond that you don't really care.

## Process

N is the number of metrics. Here N=2.

| Order  | Action  |
|--------|---------|
| 1      | Define what you want be the optimizing metric. | Here: **Accuracy** is more important |
| 2      | Define what you want be the satisficing metric and define the limited threshold. | Running time $\leqslant$ 100ms |
| 3      | Now caclulate final cost to be able to compare values. | $cost = accuracy - \frac{1}{N}\times{runningTime}=1-0.5\times{runningTime}$ |



----

For a talking clock.

|          |                                                                             |
|----------|-----------------------------------------------------------------------------|
| Accuracy | Number of False positive: (Clock says the right words but not at good time) |
| Maximize Accuracy | Number of False positive $\leqslant 1$ every 24 hours |


