<img src="../img/broadcasting_example.png" width="400" />

Principle

| Code                                                          | Broadcasting in Python                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------|
| $matrix^{m\times{n}}$ + or - or * or / $matrix^{1\times{n}}$  |         will transform the second matrix in $matrix^{m\times{n}}$. |
| $matrix^{m\times{n}}$ + or - or * or / $matrix^{m\times{1}}$  |  will transform the second matrix in $matrix^{m\times{n}}$.        |
|                                                               |                                                                    |
| $matrix^{m\times{1}}$ + or - or * or / $\mathbb{R}$           | will transform the $\mathbb{R}$ number  in $matrix^{m\times{1}}$.  |
| $matrix^{1\times{m}}$ + or - or * or / $\mathbb{R}$           | will transform the $\mathbb{R}$ number  in $matrix^{1\times{m}}$.  |

<img src="../img/broadcasting_example2.png" width="400" />
 