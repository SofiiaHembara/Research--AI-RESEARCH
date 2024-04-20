class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def array_to_tree(arr):
    """
    This function creates a complete binary tree from a given array, ensuring
    left-to-right child placement within levels.

    Args:
        arr: A list of integers representing the elements of the tree.

    Returns:
        The root node of the constructed complete binary tree.
    """
    if not arr:
        return None

    root = Node(arr[0])
    queue = [root]
    level = 0
    level_to_process = 0
    i = 1

    while i < len(arr):
    # Check for empty queue before popping (optional, for safety)
        if not queue:
            break

        current_node = queue.pop(0)
        spaces = " " * (2 ** (level + 1) - 2)  # Calculate spaces for indentation

        # Add left child if possible
        if i < len(arr):
            current_node.left = Node(arr[i])
            queue.append(current_node.left)
            print(f"{spaces}----> {current_node.left.value}")
            i += 1

        # Add right child only if there's space in the complete tree
        if i < len(arr) and 2 * level_to_process + 1 < len(arr):  # Check based on level
            current_node.right = Node(arr[i])
            queue.append(current_node.right)
            print(f"{spaces}--------> {current_node.right.value}")
            i += 1

        # Move to the next level after processing a node
        if len(queue) == 0 or queue[0].left is None:  # Check for next level
            level_to_process += 1

    return root
