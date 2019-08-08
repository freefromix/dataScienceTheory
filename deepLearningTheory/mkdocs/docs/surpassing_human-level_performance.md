# Surpassing human-level performance
## Avoidable bias when surpassing humans

### Not surpassing humans example

| Set | Error |
|-----|-------|
| Team of humans | 0.5% |
| One human | 1% |
| Training error | 0.6% |
| Dev error | 0.8% |

What is the avoidable bias?

- Avoidable bias = Training error - Team of humans = 0.6% - 0.5% = 0.1%
- Variance = Dev Error - Training error = 0.8% - 0.6% = 0.2%

### Surpassing humans example

| Set | Error |
|-----|-------|
| Team of humans | 0.5% |
| One human | 1% |
| Training error | 0.3% |
| Dev error | 0.4% |

What is the avoidable bias?

It's now actually much harder to answer that.

- 0.3% training error: Does this mean you've over-fitted by 0.2%?
- base error is 0.1%, or maybe is base error 0.2%, or maybe base error is 0.3?

|                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **We don't really know! Actually we don't have enough information to tell if you should focus on reducing bias or reducing variance in your algorithm** |

**We don't know how to make progress now.**

Moreover, if your error is already better than even a team of humans,  it's just also harder to rely on human intuition to know what we can improve.

Progress on the machine learning problem is less clear.

## Problems where ML significantly surpasses human-level performance
