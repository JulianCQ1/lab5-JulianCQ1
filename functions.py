
def promedio_estudiante(calificaciones):
    cantidad=len(calificaciones)
    if cantidad == 0:
        return 0.0  
    total = sum(calificaciones)
    promedios = total / cantidad
    return float(promedios)
