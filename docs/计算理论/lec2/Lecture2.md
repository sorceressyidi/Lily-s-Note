<font face = "Times New Roman">

# Lecture 2 - Regular Expressions
## Definition :
### Regular Expression
$a(a\cup b)^nb$ is a regular expression over $\{a,b\}$

$L(R) = \{w \in \{a,b\}^* | w\ is\ a\ string\ that\ starts\ with\ a\ and\ ends\ with\ b\}$

#### Automic Regular Expression

* $\emptyset$ : $L(\emptyset) = \emptyset$
* $a\in \Sigma$ : $L(a) = \{a\}$

#### Composition of Regular Expression

* $R_1\cup R_2$ : $L(R_1\cup R_2) = L(R_1)\cup L(R_2)$
* $R_1R_2$ : $L(R_1R_2) = L(R_1)L(R_2)$
* $R_1^*$ : $L(R_1^*) = [L(R_1)]^*$

#### Precedence of Regular Expression
* $* >  \cdot > \cup$

### Proof
#### Theorem 1: Language of Regular Expression is Regular
</font>