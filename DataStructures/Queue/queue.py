from DataStructures.List import array_list as arl

def new_queue():
    return arl.new_list()

def enqueue (my_queue, element):
    return arl.add_last(my_queue, element)

def dequeue (my_queue):
    
    if arl.is_empty(my_queue):
        raise Exception("EmptyStructureError: queue is empty")
    elemento = my_queue["elements"].pop(0) 
    my_queue ["size"]-=1
    return elemento

def peek(my_queue):
    if arl.is_empty(my_queue):
        raise Exception("EmptyStructureError: queue is empty")
    
    return arl.first_element(my_queue)

def is_empty(my_queue):
    return arl.is_empty(my_queue)

def size(my_queue):
    return arl.size(my_queue)
