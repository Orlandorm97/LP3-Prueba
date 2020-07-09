# Autor: Orlando Ramos Machuca

def determinarAprobado(promedio):
    
    if 0<=promedio<=10.4:
        print("El alumno está desaprobado.")
        
    elif 20>=promedio>=10.5:
        print("El alumno está aprobado.")
    
    else:
        print("La entrada es incorrecta.")
        
        
promedio = float(input("Ingrese el promedio: "))

determinarAprobado(promedio)