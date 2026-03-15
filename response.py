def respuesta(valor, usuario):
    if usuario < valor:
        return "Too low! Try a higher number.", False
    elif usuario > valor:
        return "Too high! Try a lower number.", False   
    else:
        return "Correct! You guessed the number!", True
    
    