from DataStructures.List import array_list as arl

def new_stack():
    return arl.new_list()

def push(my_stack, element):
    
    my_stack = arl.add_last(my_stack, element)
    return my_stack

def pop (my_stack):
    
    if arl.is_empty(my_stack):
        raise Exception("EmptyStructureError: stack is empty")
    return arl.remove_last(my_stack)

def top (my_stack):
    if arl.is_empty(my_stack):
        raise Exception("EmptyStructureError: stack is empty")
    return arl.last_element(my_stack)

def size (my_stack):
    return arl.size(my_stack)

def is_empty (my_stack):
    return arl.is_empty(my_stack)


