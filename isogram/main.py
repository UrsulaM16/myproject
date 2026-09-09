
def run(text: str) -> bool:
     # pasar la cadena a minúscula
    text = text.lower()
    # como contador
    letras_vistas = []
    # para cada carcter en texto, 
    for caracter in text:
        # Ignoramos los guiones
        if caracter == '-':
            continue
            
        # Si la letra está, no es parte del isograma
        if caracter in letras_vistas:
            return False
            
        # Guardamos la letra en nuestra lista. append guarda al final 
        letras_vistas.append(caracter)

    # Si recorrió todo sin repetir letras, sí es un isograma
    return True


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
