class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def array_to_tree(arr):
    if not arr:
        return None

    root = Node(arr[0])
    queue = [root]
    i = 1

    while i < len(arr):
        current_node = queue.pop(0)

        left_val = arr[i]
        i += 1
        if left_val is not None:
            current_node.left = Node(left_val)
            queue.append(current_node.left)

        if i < len(arr):
            right_val = arr[i]
            i += 1
            if right_val is not None:
                current_node.right = Node(right_val)
                queue.append(current_node.right)

    return root
