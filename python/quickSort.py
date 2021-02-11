def quickSort(tab,first,high):
    if len(tab) == 1:
        return tab
    if first < high:
        pi = partition(tab, first, high)
        quickSort(tab, first, pi-1)
        quickSort(tab, pi+1, high)
# ------------------------------ #
def partition(tab, first, high):
    i = (first-1)
    pivot = tab[high]
    for j in range(first, high):
        if tab[j].frequency <= pivot.frequency:
            i = i+1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[high] = tab[high], tab[i+1]
    return (i+1)
# ------------------------------ #
def quickSortIterative(tab,first,high):
    size = len(tab)
    stack = [0] * (size)
    top_stack = -1
    top_stack = top_stack + 1
    stack[top_stack] = first
    top_stack = top_stack + 1
    stack[top_stack] = high
    while top_stack >= 0:
        high = stack[top_stack]
        top_stack = top_stack - 1
        first = stack[top_stack]
        top_stack = top_stack - 1
        pi = partition( tab, first, high )
        if pi - 1 > first:
            top_stack = top_stack + 1
            stack[top_stack] = first
            top_stack = top_stack + 1
            stack[top_stack] = pi - 1
            pass
        if pi + 1 < high:
            top_stack = top_stack + 1
            stack[top_stack] = pi + 1
            top_stack = top_stack + 1
            stack[top_stack] = high
            pass
        pass
