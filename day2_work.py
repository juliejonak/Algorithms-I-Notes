def add_list(l):
    # The sum of an empty list is 0
    if l == []:
        return 0

    print(f'Add {l[0]} to the sum of {l[1:]}.')
    return l[0] + add_list(l[1:])


l = [1,2,3,4]

print(add_list(l)) # Should print 10

# add_list := element 0 + add_list(rest_of_list)


# Quick sort

sample = [5, 3, 9, 4, 8, 1, 7]


def quicksort(list):
    # One of our base cases is an empty list or list with one element
    if len(list) == 0 or len(list) == 1:
        return list

    # If we have a left list, a pivot point and a right list...
    left, pivot, right = partition(list)
    
    # Our sorted list looks like left + pivot + right, but sorted.
    # Pivot has to be in brackets to be a list, so python can concatenate all the elements to a single list
    return quicksort(left) + [pivot] + quicksort(right)

    
