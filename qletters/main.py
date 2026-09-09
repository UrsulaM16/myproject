def run(text: str) -> list[str]:
    mayusculas = []
    minusculas = []
    
    for caracter in text:
        if caracter == ' ':
            mayusculas = []
            minusculas = []
        elif caracter.isupper():
            mayusculas.append(caracter)  
        elif caracter.islower():        
            minusculas.append(caracter)

    return mayusculas + minusculas



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
