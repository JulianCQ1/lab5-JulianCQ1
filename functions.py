
def promedio_estudiante(calificaciones):
    cantidad=len(calificaciones)
    if cantidad == 0:
        return 0.0  
    total = sum(calificaciones)
    promedio = total / cantidad
    return float(promedio)
