# Orthoganization

For a supervised learning system to do well, you usually need to tune the knobs of your system to make sure that four things hold true.

- Fit training set well on cost function.
  - You have to make sure that you're at least doing well on the training set.  So performance on the training set needs to pass some acceptability assessment.
  - For some applications (it depends on your type of application), this might mean doing comparably to human level performance.
- Fit dev set well on cost function.
- Fit test set well on cost function.
- Perform well in the real world.

Imagine we use knobs to tune our issues (like the is knobs to tune your old tv):

| Issue  | Knob (Tuning parameters) |
|--------|--------------------------|
| Algorithm is not fitting the training set well | You might **train a bigger network**. Or you might **switch to a better optimization algorithm**, like the Adam optimization algorithm. Etc. **Maybe try to avoid early stopping** (see exaplanation below table)  |
| Algorithm is not fitting the dev set well. You do well on the training set but not on the dev set. | Set of knobs around **regularization**. **getting a bigger training set** would be another knob you could use, that helps your learning algorithm generalize better to the dev set. |
| Algorithm is not fitting the test set well. You do well on the dev set but not on the test set. | If it does well on the dev set but not the test set, it probably means you've overtuned to your dev set, and you need to go back and **find a bigger dev set**.  |
| Perform well in the real world | If it does well on the test set but not in the real world, then what that means is that you want to **go back and change either the dev set or the cost function**. it means that either your dev test set distribution isn't set correctly, or your cost function isn't measuring the right thing.  |

## Andrew NG tends not to use early stopping

<img src="../img/warning.png" width="20" />: And when **Andrew NG train a neural network, he tends not to use early stopping.** It's not a bad technique, quite a lot of people do it. 

But he personally finds early stopping difficult to think about. Because this is an op that simultaneously affects how well you fit the training set, because if you stop early, you fit the training set less well. 

It also simultaneously is often done to improve your dev set performance. So this is one knob that is less orthogonalized, because it simultaneously affects two things.