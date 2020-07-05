# recursive
def print_linkList_reversingly(header):
    c_node = header
    # careful, use if, instead of while
    if c_node is not None:
        print_linkList_reversingly(c_node.next)
        print(c_node.value)