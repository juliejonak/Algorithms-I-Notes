
[Lecture II Notes](#Lecture-Notes)  
a. [Pre-Class Resources](#Pre-Class-Resources)  
b. [Divide and Conquer](#Divide-and-Conquer)  


c. [O(n)](#O(n))  
d. [O(1)](#O(1))  
e. [O(n^2)](#O(n^2))  
f. [Memoization](#Memoization)  
g. [Fibonacci Numbers](#Fibonacci-Numbers)  
h. [Space Complexity](#Space-Complexity)  
i. [O(log n)](#O(log-n))  
j. [Determining Big O](#Determining-Big-O)  
k. [The 3 Main Rules of Big O](#The-3-Main-Rules-of-Big-O)  

<br>
<br>

If you found these notes helpful and want to show appreciation to the author, [coffee donations](buymeacoff.ee/G1stPBuYU) are much loved.  

<br>

# Pre-Class Resources

Additional Algorithmic Practice Problems: [Find the rotation point](practice_algs/find_rotation_point.py), [Find the smallest missing element](practice_algs/smallest_missing_element.py), and [sorted matrix search](practice_algs/sorted_matrix.py)

<br>
<br>

# Divide and Conquer

When would we use recursive solutions? Tree traversals and quick sort are instances where recursion creates an elegant solution that wouldn't be as possible iteratively.

Divide and conquer is when we take a problem, split it into the same type of sub-problem, and run the algorithm on those sub-problems.

<br>

If we have an algorithm that runs on a list, we could break the list into smaller lists and run the algorithm on those smaller lists. We will _divide_ the data into more manageable pieces.

We break down our algorithm problems into `base cases` -- the smallest possible size of data we can run our algorithm upon to determine the basic way our algorithm should work.

These solutions can give us better time complexity solutions; however, they wouldn't work if a portion of the algorithm's data is _dependent_ upon the rest. If we broke the list into two halves, and one half is required to work on the other half, we could not use recursion.

Recursion requires independent sub-data.

<br>


Let's apply recursion to breaking down what a list is. The sum of a list is equal to the first element plus the rest of the list. We could write that like in this `add_list` function found in [this file](day2_work.py):

<br>

```
def add_list(l):
    # The sum of an empty list is 0
    if l == []:
        return 0

    return l[0] + add_list(l[1:])


l = [1,2,3,4]

print(add_list(l)) # Should print 10

```

<br>

This should print 10, or the sum of the items in our list.

On each pass, the `add_list` function is taking the first item and adding the sum of the rest of the list, found by calling `add_list` on the remainder of the list. This would loop through the rest of the list in this manner, only adding together the elements once the final element was reached.

Finding a sum like this is not the most time efficient -- it would be better to do iteratively. But this allows us to understand how recursion works.

Often, iterative solutions are easier to read and more performant. 

If we add a print statement into the `add_list` function:

<br>

```

    print(f'Add {l[0]} to the sum of {l[1:]}')
    return l[0] + add_list(l[1:])
```

<br>


The terminal would print:

>Add 1 to the sum of [2, 3, 4]  
>Add 2 to the sum of [3, 4]  
>Add 3 to the sum of [4]  
>Add 4 to the sum of []  
>10  


This helps us understand what is happening at each recursive step.

Our base case is an empty list or 0, which is what we handle at the beginning of our function with returning 0 if the list is empty. By filling that in, it gives us our first return, so that each previous `add_list` call can be resolved based on the sum of the next.

<br>

When we use recursion, it uses a lot of memory, so each recursive calls allocates an amount of memory. We have a pre-set recursion limit in case we write an infinitely recursive algorithm to prevent our computer needing to reboot to end the algorithm.

With Big O, we're interested in the number of times we have to run an operation. `add_list` just runs basic addition, which is a single operation, and it is being called one time for every element in the list, so this is `O(n)`.


# Quick Sort

Quick sort is a great example use case of a recursive appropriate solution.

We need to include a base case and then call itself.

Quick sort sorts a list using `partitioning`. The partitioning process involves splitting up data around the `pivot`.

If our list is `[5, 3, 9, 4, 8, 1, 7]`. 

We'll choose a pivot point to split the list. Let's say we choose 5 as the pivot. One list will contain all the numbers less than 5, and the other will contain all the numbers greater than or equal to 5. This results in two lists like so:

> [3, 4, 1] 5 [9, 8, 7]

5 is already sorted into the correct place that it needs to be. All the numbers to the right and left of it are in the area they need to, just not yet sorted.

This process is partitioning.

<br>

Our next step is to repeat this process until we hit our base case, which is an empty list or a list with just one element. When everything is down to one element lists, then we know they are properly sorted.

> 3 and 9 are our next pivots:  
> [1] 3 [4] 5 [8, 7] 9  
> Next, 8 is our pivot:  
> [1] 3 [4] 5 [7] 8 [] 9  
> 1 3 4 5 7 8 9  

The number of sorted items doubles with each pass through this algorithm, and we have to make one complete pass through the data on each loop. That means each pass is O(n), and we have to make `log n` passes.

It takes `O(log n)` steps to pass through, with each pass taking `O(n)`, so the _average_ case is `O(n log n)`, the fastest search we can aim for.

<br>

What would be a bad case for quick sort?

[1, 2, 3, 4, 5, 6, 7]

If we look at the order of this on each loop:

> [] 1 [2, 3, 4, 5, 6, 7]  
> 1 [] 2 [3, 4, 5, 6, 7]  
> 1 2 [] 3 [4, 5, 6, 7]  
> 1 2 3 [] 4 [5, 6, 7]  
> 1 2 3 4 [] 5 [6, 7]  
> 1 2 3 4 5 [] 6 [7]  
> 1 2 3 4 5 6 7  

This took a full 7 passes, for 7 elements, because there was only one sorted item being added with each pass.

Already sorted lists are the worst case scenario which results in an order `O(n^2)`.

Quick sort shines when the first pivot chosen is roughly the median value of the list. Now, since we can't always choose the median value with the traditional quick sort.

We could use `quick select` to find the median at each step -- but this slows down our algorithm to `O(n)` run time on average.

If we choose a _random_ pivot point, we generally do not pick the worst case pivot with each pass. Randomly selecting a pivot point results in the most time efficient average.

<br>
<br>

# Implementing Quick Sort

If we were to write out our quick sort algorithm in a basic way, it would look something like this:

<br>

```
def quicksort(list):
    # One of our base cases is an empty list or list with one element
    if len(list) == 0 or len(list) == 1:
        return list

    # If we have a left list, a pivot point and a right list...
    left, pivot, right = partition(list)
    
    # Our sorted list looks like left + pivot + right, but sorted.
    # Pivot has to be in brackets to be a list, so python can concatenate all the elements to a single list
    return quicksort(left) + [pivot] + quicksort(right)
```

<br>
















