Problam : 3

Mathematically derive the average runtime complexity of the non-random pivot version of quicksort.

In the average case, the pivot splits the array into two approximately equal parts. So, k is approximately n/2, leading to:

T(n) = 2T(n/2) + O(n)

We can solve this recurrence relation using the master theorem for divide-and-conquer recurrences. The general form of the recurrence is:

T(n) = aT(n/b) + O(n^d)

In our case, a = 2, b = 2, and d = 1 (since the partitioning takes linear time O(n)).

To apply the master theorem, we compare n^d with n^(logb(a)): d = 1 logb(a) = log2(2) = 1

Since d = logb(a), we are in the case where the master theorem gives the solution:

T(n) = O(n^d logn) = O(nlogn)

The average time complexity of the non-random pivot version of Quicksort is O(nlogn). This is because, on average, the pivot splits the array into two roughly equal parts, leading to logarithmic depth of recursion, and each level of recursion requires linear time for partitioning. Therefore, the overall average runtime complexity is O(nlogn).
