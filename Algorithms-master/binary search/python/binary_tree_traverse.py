def binary_tree_mapping(depth, row_id, binary_id):
    print(depth, binary_id)
    if depth == 0:
        return
    binary_tree_mapping(depth-1, row_id//2, (row_id//2)%2)

def return_next_node(depth, row_id, binary_id, current_depth = 0):
    if depth == current_depth:
        return binary_id
    return return_next_node(depth-1, row_id//2, (row_id//2)%2, current_depth)

if __name__ == "__main__":
    print("This function maps the position of the nodes of a binary tree relating to their successor.")
    print("1 means it's on the right, 0 means left.")
    print("First row gives the depth(0 being root)")
    depth = int(input("Enter depth:"))
    id = int(input("Enter id:"))
    print("Depth | Right")
    binary_tree_mapping(depth, id, id%2)
    print("--------")
    next_move_for = int(input("Enter a row to get the relational position of the node that leads to desired id:"))
    print(return_next_node(depth, id, id%2, next_move_for))