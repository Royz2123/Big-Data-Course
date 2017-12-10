import random
import time


# returns the top k elements in the list and removes them
# the sorting occurs based on the index provided
# returns also if we should contineue
def k_select(elements, k, comparer, args=[]):
    if k >= len(elements):
        return elements, []

    # first find the kth largest element
    k_val = quickselect(elements, k, comparer, args)


    # now return all the elements that are "larger" than k
    top_k = []
    rest = []
    for elem in elements[:]:
        if comparer(elem, k_val, *args):
            top_k.append(elem)
        else:
            rest.append(elem)

    # return the top k values
    return top_k, rest


# ALGORITHM SIMILAR TO QUICKSORT

def select(lst, l, r, index, comparer, args):
    # base case
    if r == l:
        return lst[l]

    # choose random pivot
    pivot_index = random.randint(l, r)

    # move pivot to beginning of list
    lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

    # partition
    i = l
    for j in xrange(l+1, r+1):
        if comparer(lst[j], lst[l], *args):
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    # move pivot to correct location
    lst[i], lst[l] = lst[l], lst[i]

    # recursively partition one side only
    if index == i:
        return lst[i]
    elif index < i:
        return select(lst, l, i-1, index, comparer, args)
    else:
        return select(lst, i+1, r, index, comparer, args)


def quickselect(items, item_index, comparer, args):
    if items is None or len(items) < 1:
        return None

    if item_index < 0:
        raise IndexError()

    return select(items, 0, len(items) - 1, item_index, comparer, args)
