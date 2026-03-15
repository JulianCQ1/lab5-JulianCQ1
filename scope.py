
int_valor = None
str_valor = None
def set_globals(some_int, some_str):
    global int_valor, str_valor
    int_valor = some_int
    str_valor = some_str
def get_globals():
    return (int_valor, str_valor)

    
