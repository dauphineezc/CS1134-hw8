from BinarySearchTreeMap import BinarySearchTreeMap


def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()
    right_subtree_start, root = restore_bst_helper(prefix_lst, 0, len(prefix_lst) - 1)
    bst.root = root
    bst.n = len(prefix_lst)
    return bst


def restore_bst_helper(prefix_lst, start, end):
    if start > end:
        return start, None

    root_item = BinarySearchTreeMap.Item(prefix_lst[start])

    if start == end:
        return start, BinarySearchTreeMap.Node(root_item)

    right_subtree_start = end + 1

    for i in range(start + 1, end + 1):
        if prefix_lst[i] > prefix_lst[start]:
            right_subtree_start = i
            break

    left_start, left_subtree_root = restore_bst_helper(prefix_lst, start + 1, right_subtree_start - 1)
    right_start, right_subtree_root = restore_bst_helper(prefix_lst, right_subtree_start, end)

    root_node = BinarySearchTreeMap.Node(root_item)
    root_node.left = left_subtree_root
    root_node.right = right_subtree_root

    if left_subtree_root is not None:
        left_subtree_root.parent = root_node
    if right_subtree_root is not None:
        right_subtree_root.parent = root_node

    return right_start, root_node
