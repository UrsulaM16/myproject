def iluminar_puertas(corredor_str):
    # Convertir string a lista de números
    corredor = list(map(int, corredor_str.split()))
    resultado = corredor.copy()
    
    # Extraer todas las frecuencias diferentes (sin el 0)
    frecuencias = set(resultado)  
    frecuencias.discard(0)        
    
    # Para cada frecuencia
    for frecuencia in frecuencias:
        # Encontrar todas las posiciones donde aparece esta frecuencia
        posiciones = [indice for indice, valor in enumerate(resultado) if valor == frecuencia]
        
        # Verificar PARES de posiciones consecutivas
        for i in range(len(posiciones) - 1):
            inicio = posiciones[i]
            fin = posiciones[i + 1]
            
            # Extraer los valores entre inicio y fin
            medio = resultado[inicio + 1 : fin]
            
            # Verificar si TODOS son ceros
            todos_ceros = all(valor == 0 for valor in medio)
            
            # Si están todos 0, iluminar esa sección
            if todos_ceros:
                for k in range(inicio + 1, fin):
                    resultado[k] = frecuencia
    
    # Convertir de vuelta a string y retornar
    return ' '.join(map(str, resultado))

# Lee la entrada
lasers = input()
# Ejecuta la función y muestra el resultado
print(iluminar_puertas(lasers))