def heapify(tree, k):
    left, right = 2 * k + 1, 2 * k + 2
    if left < len(tree) and tree[left] > tree[k]: largest = left