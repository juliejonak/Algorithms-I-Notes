These notes are based off of Beej's previous recording for CS14, found at: https://www.youtube.com/watch?v=qBXYIBdWrhc&feature=youtu.be

# Notes Lecture I

Big O Notation is a way to determine how efficient a function is, based on run time and space requirements. It evaluates based on the _worst_ case scenario of the function. 

Even if the function might run efficiently in some instances (small item list), it will evaluate based on the worst possible set of inputs. That does not mean an algorithm can't or shouldn't be used in some scenarios - it's just important to consider, especially when building for scale.

Big O is considered the worst case evaluation while Big Theta is finds the average case.

When we discuss Big O, we're evaluating as if on a graph (see BigO Graph.png file in repo folder). It's essentially like graphing the time it takes to run the function with different sized inputs (an array of 1 item, 2 items, 3 items, etc).

The line that is shown on the graph displays the trend of that algorithm's efficiency when handling small to large inputs.

![Big O Computational Graph](BigOGraph.png "Big O Computational Graph")

## O(n)

`O(n)`, called `Order of N` or `O of N`, refers to `linear time`. Linear time means that for every additional item in the function's input, that many operations are computed. 1 input? 1 operation. 10 inputs? 10 operations. The time complexity grows linearly with the number of inputs.

On the graph image, that is depicted by the green line of `n`.

A good example of O(n) would be something like this:

```
def item_in_list(check_item, the_list):
    for item in the_list:
        if check_item == item:
            return True
    return False
```

This function receives an item and a list of items. It will pass over each individual item in the list to see if it matches with the given item. Because each item is being compared individually, the run time of this algorithm depends on how many items are in the_list. If it's short, it will be fast. If it's a long list, the run time will be much longer.

## O(1)

`O(1)`, called `Order of 1`, refers to `Constant Time`. This means that no matter how large the input is, it will always take the same amount of time to run.

On the graph image, this is depicted by the pink line of `1`.

An example of O(1) is:

```
def is_none(item):
    return item is None
```

No matter how many inputs are in `item` that we give this function, the run time will always be the same - the time it takes to return `None`. 

It cannot run faster, but it also cannot run slower. Constant time is considered the best case scenario for a function because it cannot grow despite the complexity of the inputs.


## O(n^2)

`O(n^2)`, called `Order of n squared`, indicates that for every input item (n), we have to do that number squared (n^2 or n*n) operations.

As you can imagine, that run time can become very slow, very quickly. If there are only 2 inputs, that would mean 4 operations. But if we have just 8 inputs, that's already 64 operations being computed.

On the graph image, this is depicted by the red line of `n^2`.

A common example of O(n^2) run time is a nested for loop (though that does not _always_ indicate n squared time, so consider each one carefully).

An example might be:

```
def all_combinations(the_list)
    results = []
    for item in the_list:
        for inner_item in the_list:
            results.append((item, inner_item))
    return results
```

This function matches each item within the_list with every other item in the_list. Therefore, if the_list = [1,2,3], it would output [(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)] - an output of 9 items, despite only 3 being in the input (n^2).

O(n^2) taps into Combinatorics (the mathematical study of combinations of things and counting) - but not every algorithm does, despite the common conception that most do.

Combinatorics: https://en.wikipedia.org/wiki/Combinatorics 

Discrete Math is the basis of a lot of Computer Science (if you're looking for further learning). Algebra, geometry and trigonometry are common if you're planning to go into graphics. If you like 3D graphics, Linear Algebra is a good field of additional study too.


## Memoization

`Memoization` is an optimization technique that speeds up a program or algorithm by storing the results of previous function calls in a cache, to easily access the result if the same call is made again. (This only works if, given the same input, the output is always the same.)

A `cache` is a way of storing data that typically takes extensive computing, to speed it up. It's less complete and durable than a database, so it typically only stores a subset of data. Browsers also use caching to load web pages faster, by not having to fetch and render data completely each time you re-visit a webpage. It's a way we also store user preferences.

Memoization is best used when you notice that your algorithm is making the same calculations repeatedly. A good example is when solving the Fibonacci sequence. By storing previous results, the algorithm becomes much faster (rather than having to compute the same result each time).

Another way we might use memoization is by storing square roots, sin and cosine computations within a table when the function is created, to speed up the runtime (and add to the table when new outputs are run).

If you realize a function is being called often and the run time is slow, that's a good sign that memoization would help speed it up.

If a database is being frequently queried for one or two types of input, and the table typically stays the same, to speed up the backend, we might opt to save those values and send them more quickly - rather than querying the database every time.

Further reading: https://codeburst.io/understanding-memoization-in-3-minutes-2e58daf33a19
