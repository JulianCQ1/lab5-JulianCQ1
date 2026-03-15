def list_shift(listas,float):
    for i in range(len(listas)):
        listas[i] += float

def calc_avg(listas):
    total = sum(listas)
    cantidad = len(listas)
    return total / cantidad
def print_normalized(listas):
    print(listas)
    
   