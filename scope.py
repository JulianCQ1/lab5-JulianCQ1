
int_valor = None
str_valor = None
def set_globals(some_int, some_str):
    global tupla
    int_valor = some_int
    str_valor = some_str 
    tupla = (int_valor, str_valor)
def get_globals():
    return tupla

    
