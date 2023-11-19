## Graphs

### Some defs

* Complete graphs

  > $Undirected \ V=n \ \ \ \  E=C_n^2=\frac{n(n-1)}{2}$

  > $Directed \ V=n \ \ \ \  E=2*C_n^2=n(n-1)$

* Adjacent

> $Undirected \ : (v_i,v_j)\ is \ incident \ on\ v_i\ and\ v_j$

> $Directed \ : v_i \ is\ adjacent\ to \ v_j \ \ \ \  \ v_j \ is\ adjacent\ from \ v_i$

* Subgraph

* Simple Path

* Connected

  > $Undirected: $  An undirected graph G is connected if every pair of distinct $v_i$ and $v_j$ are connected
  >
  > * A tree = a graph that is connected and acyclic.

  > $Directed: $  
  >
  > > Strongly connected directed graph G = for every pair of $v_i$ and $v_j$ in V( G ), there exist directed paths from $v_i$ to $v_j$ and from $v_j$ to $v_i$. 
  > >
  > >  If the graph is connected without direction to the edges, then it is said to be weakly connected
  >
  > > Strongly connected component :  the maximal subgraph that is strongly connected
  >
  > * A DAG = a directed acyclic graph.

* Degree: Number of edges incident to v.
  * For a directed G, we have in-degree and out-degree. 

### Representation of Graphs

#### Adjacency Matrix

$adj_- mat[i][j]=\left\{\begin{array}{l} 1 \ if (v_i,v_j) \ or <v_i,v_j> \in E(G)\\0\ \ otherwise \end{array}\right.$

> If G is undirected the matrix is symmetric,thus sorting only half of the matrix

> > The trick is to store the matrix as a 1-D array: adj_mat [ $n(n+1)/2 $] = ${ a_{11}, a_{21}, a_{22}, ..., a_{n1}, ..., a_{nn} }$
>
> > The index for $a_{ij}$  is  $ i  ( i - 1 ) / 2 + j $.

$\begin{align*}degree(i) &= \sum_{j=0}^{n-1}adj_-mat[i][j] \ (If\ G\ is\ undirected)\\ & \ \ +\sum_{j=0}^{n-1}adj_-mat[j][i]\ (If\ G\ is\ directed)\end{align*}$

#### Adjacency Lists

* Undirected

![1](1.png)

> Degree( $i$ ) = number of nodes in graph[ $i$ ] (if $G$ is undirected).
>
> T of examine (whether complete)  E(G) = O( n + e ) 

* Directed

A. Add inverse adjacency lists

B.Multilists

#### Adjacency Multilist

![2](2.png)

![4](4.png)



* The space taken :$ (n+2e)$ ptrs + $2e$ ints  and “mark” is not counted
* Sometimes we need to mark the edge after examine it,and then find the next edge.This representation makesit easy to do so.

### Topological Sort

#### AOV Network

Digraph G in which V( G ) represents activities ( e.g.  the courses ) and E( G ) represents precedence relations

* i  is a predecessor of j $:$ there is a path from i  to j 
* i  is an immediate predecessor of  j $:$   < i,  j > $\in$ E( G )  then $j$ is called a successor ( immediate successor ) of i
* Partial order $:$ a precedence relation which is both transitive and irreflexive.

> If the precedence relation is reflexive, then there must be an i such that i is a predecessor of i.  
>
> That is, i must be done before i is started.   Therefore if a project is feasible, it must be irreflexive.

* Feasible AOV network must be a dag (directed acyclic graph).

####  topological order

A topological order is a linear ordering of the vertices of a graph such that, for any two vertices, i, j, if i is a predecessor of j in the network then i precedes j in the linear ordering.

* Test an AOV for feasibility, and generate a topological order if possible.

* Method One

  $O(|V|^2)$

```C
void Topsort( Graph G )
{   int  Counter;
    Vertex  V, W;
    for ( Counter = 0; Counter < NumVertex; Counter ++ ) {
	V = FindNewVertexOfDegreeZero( );
	if ( V == NotAVertex ) {
	    Error ( “Graph has a cycle” );   break;  }
	TopNum[ V ] = Counter; /* or output V */
	for ( each W adjacent to V )
	    Indegree[ W ] – – ;
    }
}
```

* Method Two

```C
void Topsort( Graph G )
{   Queue  Q;
    int  Counter = 0;
    Vertex  V, W;
    Q = CreateQueue( NumVertex );  MakeEmpty( Q );
    for ( each vertex V )
	if ( Indegree[ V ] == 0 )   Enqueue( V, Q );
    while ( !IsEmpty( Q ) ) {
	V = Dequeue( Q );
	TopNum[ V ] = ++ Counter; /* assign next */
	for ( each W adjacent to V )
	    if ( – – Indegree[ W ] == 0 )  Enqueue( W, Q );
    }  /* end-while */
    if ( Counter != NumVertex )
	Error( “Graph has a cycle” );
    DisposeQueue( Q ); /* free memory */
}
```

### Shortest Path Problem

#### 1.Single-Source Shortest Path Problem

* Unweighted Shortest Path

```C
void unweighted(Table T){
  	int CurrDist;
  	Vertex V,W;
  	 for(CurrDist=0;CurrDist<NumVertex;CurrDist++){
      for(each vertex V){      if(!T[V].Known&&T[V].Dust==CurrDist){
          R[V].Known=true;
          for(each W adjacent to V){
            if(T[W].Dist==infinity){
              T[W].Dist=CurrDist+1;
                T[E].Path=V;
            }
          }
        }
      }
    }
}
```

But the time complexity is $O(|V|^2)$

* Note: If V is unknown yet has $Dist < Infinity$,then Dist is either $CurrDist$ or $CurrDist +1$(Remember Tree?)

> Improvement

```C
void unweighted (Table T){
  Queue Q;
  Vertex V,W;
  Q=CreateQueue(NumVertex);MakeEmpty(Q);
  Enqueue(S,Q);
  while(!isEmpty(Q)){
    V=Dequeue(Q);
    T[V].known=true;//not really necessary
    for(each W adjacent to V){
      if(T[W].Dist==Infinity){
        T[W].Dist=T[V].Dist+1;
        T[W].Path=V;
        ENqueue(W,Q)
      }
    }
  }
  DisposeQueue(Q);
}
```

* $T=O(|V|+|E|)$

#### Dijkstra's Algorithm(for weighted shortest paths)

```C
void Dijkstra(Table T){
  //T is initialized by Figure 9.30 on p 303
  Vertex V,W;
  for(;;){
    V=smallest unknown distance vertex;
    if(V==NotAVertex){break;}
    T[V].known=true;
    for(each W adjacent to V){
      if(!T[W].Known){
        if(T[V].Dist+Cvw<T[W].Dist){
          Decrease(T[W].Dist to T[V].Dist+Cvw);
          T[W].Path=V
        }
      }
    }
  }
}
```

