from BinarySearchTreeMap import BinarySearchTreeMap


def create_chain_bst(n):
    tree = BinarySearchTreeMap()
    for i in range(n):
        tree.insert(i + 1, None)
    return tree


def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst


def add_items(bst, low, high):
    if low > high:
        return bst
    mid = (low + high) // 2
    bst.insert(mid, None)
    add_items(bst, low, mid - 1)
    add_items(bst, mid + 1, high)




