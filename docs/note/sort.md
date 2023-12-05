## Simple Sort

### Algorithm

#### Bubble sort

> Basic

```C
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
```

> Improvement

```C
void bubbleSort_recursive(int a[],int begin,int end,int n){
    if(end>begin){
        int lastswap=-1;
        for(int i=begin;i<end;i++){
        if(a[i]>a[i+1]){
          int m=a[i];
          a[i]=a[i+1];
          a[i+1]=m; 
          lastswap=i;
        }
    }
    end=lastswap;
    sort(a,begin,end,n);
}
  
void bubbleSort_iter (int a[], int n){
    int lastswap, end;
    for (int i=0;i<n-1;i++) {
        lastswap = -1;
        for (int j=0;j<end;j++) {
            if (a[j] > a[j + 1]) {
                exchange(&a[j], &a[j + 1]);
                lastswap = j;
            }
        }
        end = lastswap;
    }
}
```

#### Selection sort

```C
void selectionSort(int arr[], int n) {
    int i, j, min_idx;
    // 外层循环遍历未排序部分
    for (i = 0; i <n-1;i++) {
        // 假设当前未排序部分的第一个元素为最小
        min_idx = i;
        // 内层循环在未排序部分中找到最小元素的索引
        for (j=i+1;j<n;j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        // 将找到的最小元素与未排序部分的第一个元素交换位置
        swap(&arr[min_idx], &arr[i]);
    }
}
```

#### Insertion Sort

```C
void InsertionSort ( ElementType A[ ], int N ){
  int j,P;
  ElementType Tmp;
  for(P=1;P<N;P++){
    Tmp=A[p];
    for(j=P;j>0&&A[j-1]>Tmp;j--){
      A[j]=A[j-1];
    }
    A[j]=Tmp;
  }
}
```

The worst case:Input $A[ \ \ ]$ is in reverse order.   $T( N ) = O( N^2 )$

### Analysis

* A Lower Bound for Simple Sorting Algorithms
  * An inversion in an array of numbers is any ordered pair $( i, j )$ having the property that $i < j$ but $A[i] > A[j]$.
  * Swapping two adjacent elements that are out of place removes exactly one inversion.
  * $T ( N, I )$ = $O( I+N  )$ where $I$ is the number of inversions in the original array.

* The average number of inversions in an array of N distinct numbers is  $N ( N +1 ) / 4$.
  * Any algorithm that sorts by exchanging adjacent elements requires $\Omega( N^2 )$ time on average.

### Shell sort

```C
void shellSort(int arr[], int n) {
    // 选择增量序列，可以根据实际情况选择不同的增量序列
    for (int gap = n / 2; gap > 0; gap /= 2) {
        // 对每个增量进行插入排序
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            // 在每个子数组中执行插入排序
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            // 将temp插入到正确位置
            arr[j] = temp;
        }
    }
}
```

### Heap Sort

