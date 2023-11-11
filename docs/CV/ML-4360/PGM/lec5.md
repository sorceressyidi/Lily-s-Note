# Probabilistic Graphical Models

## Structured Prediction

### Spatial regularization

$p(D)\propto e^{-\sum_i\phi_{data}(d_i)-\lambda\sum_{(i，j)\in S}\phi_{smooth}(d_i,d_j)}$

- i~j neighbouring pixels (on a 4-connected grid). 
- $\phi_{smooth} $ is a regularization term that encourages neighboring pixels to have similar disparities.

> $\phi_{data}(di) =min(|I(xi, yi) - J(xi - di, yi)|, σ)$
>
> $\phi_{smooth} (di,dj) = min(|di - dj|,τ)$
>
> > where$I$and $J$ are the image pairs
> >
> > $σ$ and $τ$ are truncation thresholds.

- **Structured Prediction:**

> Probabilistic graphical models encode local dependencies of the problem
>
> Deep neural netwoks with image-based outputs (stereo, flow, semantics)

## Markov Random Fields

#### Undirected graphical models (UGM)

- Pairwise (non-causal) relationships
- Can write down model, and score specific configurations of the graph, but no explicit way to generate samples
- Contingency constrains on node configurations

#### cliques

Refers to fully connected subgraphs in a graphical model, particularly in models like Markov Random Fields or Conditional Random Fields.

In this context, a clique is a group of nodes in a graph where every pair of nodes is directly connected.

#### potential

- A **potential**  $φ(x)$is a non-negative function of the variable x
- A **joint potential** $φ(x1, x2, . . . )$ is a non-negative function of a **set** of variables.

#### Definations of an undirected graphical model

$(P(x_1……x_n)=\frac{1}{Z}\prod_{c\in C}\phi_c(x_c)$

$(Z = \sum_{x_1……x_n}\prod_{c\in C}\phi_c(x_c)$

#### Defination of Markov Random Field

- For a set of variables $X ={x_1,...,x_M}$, a **Markov Random Field** is defined as a product of potentials over the **(maximal) cliques** ${(X_k)}_{k=1}^K$of the undirected graph G

  $p(X)=\frac{1}{Z}\prod_{k=1}^K\phi_k(X_k)$

- $Z$normalizes the distribution and is called **partition function**
- Examples：

![1](1.png)

#### Properties

$Condition \ One$

![2](2.png)

- Marginalizing over c makes a and b dependent

$Proof$

![3](3.png)

![4](4.png)

- Explain:take $\sum_c\phi_1(a,c)\phi_2(b,c)$ for example()
- Conditioning on c makes a and b independent

$Proof$

![5](5.png)

- Global Markov Property

> Markov blanket

#### Hammersley-Clifford Theorem

A probability distribution that has a **strictly positive mass** or density satisfies the **Markov properties** with respect to an undirected graph G if and only if it is a Gibbs random field, i.e., its density can be **factorized** over the (maximal) cliques of the graph.

![6](6.png)

![7](7.png)

## Factor Graphs

![8](8.png)

$p(X) = \frac{1}{Z}\prod_{k=1}^Kf_k(X_k)${k=1}^K $

## Belief Propagation

### Inference in Chain Structured Factor Graphs

![9](9.png)

$p(a, b, c, d) = \frac{1}{Z}f_1(a, b)f_2(b, c)f_3(c, d)f4(d)$

$p(a,b,c) = \sum_{d}p(a,b,c,d)$

$\ \ \ \ \ \ \ \ \ \ \ \ \ \ = \frac{1}{Z}f_1(a,b)f_2(b,c)\underbrace{\sum_{d}f_3(c,d)f_4(d)}_{μ_{d→c}(c)}$

$p(a,b) = \sum_{c}p(a,b,c)$

$\ \ \ \ \ \ \ \ \ \ = \frac{1}{Z}f_1(a,b)\underbrace{\sum_{c}f_2(b,c)μ_{d→c}(c)}_{μ_{c→b}(b)}$

$……$

### Inference in Tree Structured Factor Graphs

![10](10.png)



![11](11.png)

### Sum-Product Algorithm

#### Belief Propagation:

- Algorithm to compute all messages efficiently
- Assumes that the graph is singly-connected (chain, tree)

#### Algorithm:

- Initialization
- Variable to Factor message
- Factor to Variable message
- Repeat until all messages have been calculated
- Calculate the desired marginals from the messages

#### Log Representation

![12](12.png)

![13](13.png)

#### Max-Product Algorithm

## Examples