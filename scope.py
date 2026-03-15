int_valor = None
str_valor = None
def set_globals(some_int, some_str):
    global tuple
    int_valor = some_int
    str_valor = some_str 
    tuple = (int_valor, str_valor)
def get_globals():
    return tuple

    
