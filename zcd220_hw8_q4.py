def find_min_abs_difference(bst):
    if not bst.root:
        return None

    min_difference = float("inf")
    prev_val = None

    def inorder_traversal(node):
        nonlocal min_difference, prev_val

        if not node:
            return
        inorder_traversal(node.left)

        if prev_val is not None:
            min_difference = min(min_difference, abs(node.item.key - prev_val))

        prev_val = node.item.key
        inorder_traversal(node.right)

    inorder_traversal(bst.root)
    return min_difference
