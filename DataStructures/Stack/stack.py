from DataStructures.Stack import stack as st
def new_stack():
    stack = st.new_stack
    return stack

def push(stack,element):
    stack = stack.push(stack,element)
    return stack

def pop (stack):
    elemento = st.pop(stack)
    return elemento
        
def is_empty(stack):
    if stack == []:
        resp = False
    else: 
        resp = True
    return resp

def top(stack):
    i = size
    elemento_en_el_tope = stack[0]
    return elemento_en_el_tope

def size(stack):
    tamanio = len(stack)
    return tamanio