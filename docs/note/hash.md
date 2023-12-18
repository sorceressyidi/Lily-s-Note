# HASHING
## Interpolation Search

Interpolation Search is a searching algorithm used to find a specific element in a sorted array. Similar to binary search, it employs a divide-and-conquer strategy, but it differs by estimating the probable position of the target value based on the distribution of the search key and array elements at each step.

The algorithm proceeds as follows:

1. Assume the array is sorted.

2. Calculate the interpolation position using the formula:

   $position=low+⌊\frac{(high−low)×(key−arr[low])}{arr[high]−arr[low]⌋}$

   Here, $arr$ is the array, and $low$ and $high$ are the array indices, while $key$ is the element to be searched.

3. If $arr[position]=key$, the target element is found, and the position positionposition is returned.

4. If $arr[position]<key$, continue the search in the right half by updating $low=position+1$

5. If $arr[position]>key$, continue the search in the left half by updating $high=position−1$

6. Repeat steps 2 to 5 until the target element is found or $low>high$.

Interpolation Search excels when dealing with uniformly distributed sorted arrays, as it efficiently estimates the target element's position, reducing the number of search iterations. However, its effectiveness relies on the assumption of a roughly uniform distribution of array elements. In cases of uneven data distribution, other search algorithms may outperform Interpolation Search. Binary search, for instance, could be more stable as it is less sensitive to the distribution of array elements.

### Hash Tables

https://www.geeksforgeeks.org/hashing-data-structure/#introduction
