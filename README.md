# :construction: groupem

🙋 Grouping people so everyone is happy.

If you've ever had to group people together (esp. kids) and everyone wanted something different, you know it's a pain. This small programm tries to remove the hassle doing that.

<!-- TODO -->

## Installation and Usage

This project is build in python 3.6, so make sure you have python 3 installed (at least nobody has tried running this in python 2.x)

Then just clone this repo

```shell
git clone https://github.com/jonathanvoelkle/GroupEm.git
```

and change the input file (optional, see the following).

The programm tries to locate a file `data/data.csv` (with has to have the said structure).

A sample dataset is provided under [`sample/data.csv`](/sample/data.csv).

Note that a set of data with a large number people or large group-variability can take a (very, very) long time to process, you might have to modify this algorithm.

## Specification and Implementation

### General assumptions and definitions

So we want to split a set of $n$ people $P = (p_1, \dots, p_n)$ into a set of $k$ groups $G = (g_1, \dots, g_k)$ ($k \leq n)$.

Each person $j$ has a set of preferences $v_j$ regarding the groups
$$v_j : G \to [0,1] \quad \forall j \in \{ 1, \dots, n \}$$

We set
$$g_1 \succsim g_2 \Leftrightarrow v(g_1) \geq v(g_2)$$

Our goal is to maximize the overall satisfaction $S$ by trying to meet the preferences of the individual person. How the total satisfactions is determinined has to be futher decided.

### [Hungarian algorithm](https://en.wikipedia.org/wiki/Hungarian_algorithm) $\mathcal{O} (n^4)$

Assume $k = n$, so we have a matrix.
Colums = $P$,
Rows = $G$.

$$
\begin{pmatrix}
v_1(g_1) & v_2(g_1) & \cdots & v_n(g_1) \\
v_1(g_2) & v_2(g_2) & \cdots & v_n(g_2) \\
\vdots & \vdots & \ddots & \vdots \\
v_1(g_n) & v_2(g_n) & \cdots & v_n(g_n)
\end{pmatrix}
$$

[`scipy`](https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.optimize.linear_sum_assignment.html) include a implementation for this problem

```python
solution = scipy.optimize.linear_sum_assignment(M)
```

### Further modifications

This algorithm has to be run multiple times, to consider flexible group sizes.
Which group-size is the best, has to be evaluated through $S(solution)$.
<!-- TODO -->

The code uses a integer based rating system (e.g. stars, higher value means higher preferences) (not the propsed 0 to 1 interval) and transforms them into a cost function to be used in `linear_sum_assignment()`.

## FAQ

<dl>
  <dt>The math in this doc looks weird</dt>
  <dd>Yeah, I know [#3](https://github.com/jonathanvoelkle/GroupEm/issues/3) (If you know a solution, let me know, or submit a PR)</dd>

  <dt>I found a bug/have a idea for improvement/etc</dt>
  <dd>Feel free to submit a PR</dd>
</dl>

## Copyright and License
