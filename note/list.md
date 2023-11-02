## linked list
```C
// Reverse a linked list
q=h;
p=NUll;
while(q){
    t = q->next;
    q->next = p;
    p=q;
    q=t;
}
h = p;

LNode *reverse( LNode *head ){
    LNode *p0,*head1;
    head1=NULL;
    for(p0=head->next;p0;){
       LNode *temp=p0->next;//important!!!
       p0->next =head1;
       head1=p0;
       p0=temp;
    }
    return head1;
}
```
* multilist
* sparse matrix representation