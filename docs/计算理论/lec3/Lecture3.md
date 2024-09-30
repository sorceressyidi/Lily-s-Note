<font face = "Times New Roman">

# Lecture 3 - Context-Free Grammar CFG

A context-free grammar (CFG) is a set of recursive rules used to generate patterns of strings. 
A CFG $G = (V, \Sigma, R, S)$ consists of:

- A finite set of variables (non-terminal symbols) $V$.
- A finite set of terminal symbols $\Sigma$.
- S $\in$ $V-\Sigma$ is the start symbol.
- R $\in$ $(V-\Sigma) \times (U)^*$ is a finite set of rules.

* Define in one step: 
* derivation
* G generates $w\in \Sigma^*$ if $S \Rightarrow^* w$.
  * L(G) = {w $\in \Sigma ^*$| G generates w} is a context-free language.

**Example:**

* $\{a^nb^n|n\geq 0\}$ is a context-free language.
  * Rule: $S \rightarrow aSb | e$.
* $\{w\in {a,b}^*|w = w^R\}$ is a context-free language.
  * Rule: $S \rightarrow aSa | bSb | e | a | b$.
</font>