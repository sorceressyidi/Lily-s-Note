<font face = 'Times New Roman'>

## Leftist Heaps

### Definition

#### Def.1

The null path length, $Npl(X)$, of any node $X$ is the length of the shortest path from $X$ to a node without two children.  Define $Npl(NULL) = –1$.

#### Def.2

The leftist heap property is that for every node $X$​ in the heap, the null path length of the left child is at least **as large as** that of the right child.

#### Theorem.1

A leftist tree with $r$ nodes on the right path must have at least $2^r – 1$​ nodes.

* For right subtree

  **For the tree,left path actually all equals to its roots' NPL**

  1. $r=1$ clearly holds

  2. If $NLP(X)=r\le k$ holds then if $NLP(X)=r=k+1:$​ 

     Its right subtree must have $NLP(X)=k$

     $\because when\ NLP(X)= k \ right \ path \ has \ at\ least\  2^k-1\ nodes$​

     So all the right part at least $2^k-1$

* For left subtree

  1. $r=1$ clearly holds

  2. If $NLP(X)\le k$ holds then if $NLP(X)=k+1:$ 

     Its left subtree's right path must be $\ge k$​

     So at least right path is k, so at least $2^k-1$ for the left part

* Thus $2^k-1+2^k-1+1=2^{k+1}-1$​

* Induction concludes.

### Operations

#### Merge

![1](1.png)

* Recursive Version.

```C
PriorityQueue  Merge ( PriorityQueue H1, PriorityQueue H2 ){ 
	if ( H1 == NULL )   return H2;	
	if ( H2 == NULL )   return H1;	
	if ( H1->Element < H2->Element ){return Merge1( H1, H2 );} 
	else {return Merge1( H2, H1 );}
}
static PriorityQueue
Merge1(PriorityQueue H1,PriorityQueue H2){
  if(H1->Left == NULL){H1->Left = H2;}
  else{
    H1->Right = Merge(H1->Right,H2);
    if(H1->Left->Npl<H1->Right->Npl){
      	swapChildren(H1);
    }
    H1->Npl = H1->Right->Npl+1;
  }
  return H1;
}
```

* $T_p=O(logN)$​

* Iterative Version

  ![2](2.png)

* For **SORTING** $loglogN$ --> $logN * loglogN$

* Only have to maintain two pointers.

## Skew Heaps

Any $M$ consecutive operations take at most $O(M log N)$ time.

* **Merge**:

   Always swap the left and right children except that the largest of all the nodes on the right paths **does not have its children swapped**.  $No Npl.$

  ![3](3.png)

  Skew heaps have the advantage that no extra space is required to maintain path lengths and no tests are required to determine when to swap children.

  It is an open problem to determine precisely the expected right path length of both leftist and skew heaps.

### Amortized Analysis for Skew Heaps

$D_i =$  the root of the resulting tree.

$\Phi(D_i)=$​​​  **number of heavy nodes.**

> $\Phi(D_i) =$number of  right nodes?
>
> No! Think of only operation where num of right nodes will decrease: will not happen because  the largest of all the nodes on the right paths **does not have its children swapped**
>
> So this $\Phi(D_i)$ will always be increasing.

#### Def:

A node $p$ is heavy if the number of descendants of $p$’s right subtree is at least half of the number of descendants of $p$, and light otherwise.  

**Note that the number of descendants of a node includes the node itself.**

![4](4.png)

1. $T_{worst}=$all right nodes $=l_1+h_1+l_2+h_2$

2. All heavy points at the right path will **ALWAYS** turn into light points.

3. Original light points **at most** can **ALL turn into heavy nodes**.

   Remember: also need to insert into left subtrees.

4. h is heavy nodes on the left paths,**will note change**,cause its descandents will never **exchange**! .

5. Therefore Credits = $l_1+l_2-h_1-h_2$​​​.

6. $T_{amotized}= T_{worst}+credits \le2(l_1+l_2)$​

7. $l_{right}=O(logN)$​​ ? -- Actually if we want $l_{right}$ to be large ,best almost balanced.

   > 假如root的左subtree 很多，把多出来的给右边来增加右链长，这样左右node一样，且右node的heavy nodes至少不会少.

### Amortized Analysis

* Introduction to Algorithms

## Binomial Queue

![5](5.png)

* $B_k$ structure + heap order + one binomial tree for each height

  $\therefore$ A priority queue of **any size** can be uniquely represented by a collection of binomial trees.

  > Example : $13=2^0+2^2+2^3=1101_2$

### Operations

#### FindMin

The minimum key is in one of the roots.

There are at most $「logN$  roots, hence $T_p = O( logN)$​​.

> 二进制分解，所以$logN$

* We can remember the minimum and update whenever it is changed.  

  Then this operation will take $O(1)$​.

#### Merge

![6](6.png)

* To combine two trees $O(1)$

* At most $O(logN)$ times

  **! Must keep the trees in the binomial queue sorted by height.**

#### Insert

![7](7.png)

#### DeleteMin

![8](8.png)

### Implementation

```C++
typedef struct BinNode *Position;
typedef struct Collection *BinQueue;
typedef struct BinNode *BinTree;  /* missing from p.176 */

struct BinNode 
{ 
	ElementType	    Element;
	Position	    LeftChild;
	Position 	    NextSibling;
} ;

struct Collection 
{ 
	int	    	CurrentSize;  /* total number of nodes */
	BinTree	TheTrees[ MaxTrees ];
} ;
```

```C++
BinTree CombineTrees( BinTree T1, BinTree T2 )
{  /* merge equal-sized T1 and T2 */
	if ( T1->Element > T2->Element )
		/* attach the larger one to the smaller one */
		return CombineTrees( T2, T1 );
	/* insert T2 to the front of the children list of T1 */
	T2->NextSibling = T1->LeftChild;
	T1->LeftChild = T2;
	return T1;
}
```

$T_p = O( 1 )$​

```C++
BinQueue  Merge( BinQueue H1, BinQueue H2 )
{	BinTree T1, T2, Carry = NULL; 	
	int i, j;
	if ( H1->CurrentSize + H2-> CurrentSize > Capacity )  ErrorMessage();
	H1->CurrentSize += H2-> CurrentSize;
	for ( i=0, j=1; j<= H1->CurrentSize; i++, j*=2 ) {
	    T1 = H1->TheTrees[i]; T2 = H2->TheTrees[i]; /*current trees */
	    switch( 4*!!Carry + 2*!!T2 + !!T1 ) { 
        case 0: /* 000 */ /* Carry T1 T2 */
        case 1: /* 001 */  break;	
        case 2: /* 010 */  H1->TheTrees[i] = T2; H2->TheTrees[i] = NULL; break;
        case 4: /* 100 */  H1->TheTrees[i] = Carry; Carry = NULL; break;
        case 3: /* 011 */  Carry = CombineTrees( T1, T2 );
                      H1->TheTrees[i] = H2->TheTrees[i] = NULL; break;
        case 5: /* 101 */  Carry = CombineTrees( T1, Carry );
                      H1->TheTrees[i] = NULL; break;
        case 6: /* 110 */  Carry = CombineTrees( T2, Carry );
                      H2->TheTrees[i] = NULL; break;
        case 7: /* 111 */  H1->TheTrees[i] = Carry; 
                      Carry = CombineTrees( T1, T2 ); 
                      H2->TheTrees[i] = NULL; break;
	    } /* end switch */
	} /* end for-loop */
	return H1;
}
```



```C++
BinQueue  Merge( BinQueue H1, BinQueue H2 )
{	BinTree T1, T2, Carry = NULL; 	
	int i, j;
	if ( H1->CurrentSize + H2-> CurrentSize > Capacity )  ErrorMessage();
	H1->CurrentSize += H2-> CurrentSize;
	for ( i=0, j=1; j<= H1->CurrentSize; i++, j*=2 ) {
	  T1 = H1->TheTrees[i]; T2 = H2->TheTrees[i]; /*current trees */
	  switch( 4*!!Carry + 2*!!T2 + !!T1 ) { 
		case 0: /* 000 */
	 	case 1: /* 001 */  break;	
		case 2: /* 010 */  H1->TheTrees[i] = T2; H2->TheTrees[i] = NULL; break;
		case 4: /* 100 */  H1->TheTrees[i] = Carry; Carry = NULL; break;
		case 3: /* 011 */  Carry = CombineTrees( T1, T2 );
			            H1->TheTrees[i] = H2->TheTrees[i] = NULL; break;
		case 5: /* 101 */  Carry = CombineTrees( T1, Carry );
			            H1->TheTrees[i] = NULL; break;
		case 6: /* 110 */  Carry = CombineTrees( T2, Carry );
			            H2->TheTrees[i] = NULL; break;
		case 7: /* 111 */  H1->TheTrees[i] = Carry; 
			            Carry = CombineTrees( T1, T2 ); 
			            H2->TheTrees[i] = NULL; break;
	    } /* end switch */
	} /* end for-loop */
	return H1;
}
```

* 不枚举？

  > 哨兵

```C++
BinQueue  Merge( BinQueue H1, BinQueue H2 ){
  
}
```

* DeleteMin

```C++
ElementType  DeleteMin( BinQueue H ){
  BinQueue DeletedQueue; 
	Position DeletedTree, OldRoot;
	ElementType MinItem = Infinity;  /* the minimum item to be returned */	
	int i, j, MinTree; /* MinTree is the index of the tree with the minimum item */
	if ( IsEmpty( H ) )  {  PrintErrorMessage();  return –Infinity; }
	for ( i = 0; i < MaxTrees; i++) {  /* Step 1: find the minimum item */
	    if( H->TheTrees[i] && H->TheTrees[i]->Element < MinItem ){ 
				MinItem = H->TheTrees[i]->Element;  MinTree = i;    
      } /* end if */
	} /* end for-i-loop */
  
	DeletedTree = H->TheTrees[MinTree];  
	H->TheTrees[MinTree] = NULL;   /* Step 2: remove the MinTree from H => H’ */ 
	OldRoot = DeletedTree;   /* Step 3.1: remove the root */ 
	DeletedTree = DeletedTree->LeftChild;   free(OldRoot);
	DeletedQueue = Initialize();   /* Step 3.2: create H” */ 
	DeletedQueue->CurrentSize = (1<<MinTree ) – 1;  /* 2MinTree – 1 */
	for ( j = MinTree – 1; j >= 0; j – – ) {  
	    DeletedQueue->TheTrees[j] = DeletedTree;
	    DeletedTree = DeletedTree->NextSibling;
	    DeletedQueue->TheTrees[j]->NextSibling = NULL;
	} /* end for-j-loop */
  
	H->CurrentSize  – = DeletedQueue->CurrentSize + 1;
	H = Merge( H, DeletedQueue ); /* Step 4: merge H’ and H” */ 
	return MinItem;
}
```

* A binomial queue of $N$ elements can be built by $N$ successive insertions in $O(N)$​ time.

  ![9](9.png)

  * $1/2$ no merge
  * $1/4$ one merge
  * $1/8$ two merges..
  * $1/16$ three merges...

  ![10](10.png)

</font>
