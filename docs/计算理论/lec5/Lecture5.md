<font face = "Times New Roman">

# Lecture 5 - Turing Machine

## Turing Machine

A Turing machine is a mathematical model of computation that defines an abstract machine. It was invented by Alan Turing in 1936. A Turing machine can simulate the logic of any computer algorithm, and is therefore the theoretical foundation of all modern computers.

A Turing machine is a 5-tuple $(K, \Sigma, \delta, s, H)$, where:

- $K$ is a finite set of states.
- $\Sigma$ is a finite set of symbols.
- s $\in$ $K$ is the start state.
- $H$ $\in$ $K$ is the halt state.
- $\delta$ is the transition function, which maps $(K - H)(\text{current state}) \times \Sigma$ to $K (\text{next state})\times (\Sigma(\text{write})\cup\{L,R\}(\text{moving}))$.

The transition function $\delta$ satisfies the following properties:

* $\forall q \in K - H, \delta(q,\triangleright) = (p,L)$ for some $p \in K$.
* $\forall q \in K - H, \forall a \in \Sigma, if\ \delta(q,a) = (p,b,D)$, then $b \neq \triangleright$.

leftend $\triangleright$ is a special symbol that is used to indicate the left end of the tape.

blank symbol $\cup$ is a special symbol that is used to indicate the blank symbol.
### configuration

A configuration of a Turing machine is a member of 

$$(K \times \triangle(\Sigma-\{\triangleright\})^*) \times ((\Sigma-\{\triangleright\})^* (\Sigma - \{\triangleright,\cup\})\cup \{e\}).$$

* $\Sigma - \{\triangleright,\cup\}$ is the last symbol that is not $\cup$
* {e} represents the following all symbols are $\cup$.

We say $(q,\triangleright w_1au_1) \vdash_M (q_2,\triangleright w_2a_2u_2)$ if 

* writing : $\delta(q_1,a_1) = (q_2,a_2) and a_2 \in \Sigma - \{\triangleright\}$ and $w_2 = w_1$ and $u_2 = u_1$.

* moving left : $\delta(q_1,u_1) = (q_2,L)$ and $w_1=w_2a_2$ and $u_2 = a_1u_1$.

M halts if it reaches **a halting configuration**

### Acceptance and Rejection

A Turing machine M accepts a string w if $(s,\triangleright\cup w) \vdash^* (yes,\triangleright\cup aw)$ 

A Turing machine M rejects a string w if $(s,\triangleright\cup w) \vdash^* (no,\triangleright\cup aw)$

Given a Turing machine M, we can define the language accepted by M as $L(M) = \{w \in \Sigma^* | M \text{ accepts w}\}$.

M decides a language $L$ if M accepts all strings in L and rejects all strings not in L.

M semi-decides a language $L$ if M accepts all strings in L and may loop (or reject) on strings not in L.

### Example

* $L = \{a^nb^nc^n|n\geq 0\}$ can be decided by a Turing machine.


</font>