import re # descarga modulo de expresiones(busca y manipula patrones de texto)

def run(input_path: str) -> str:
    longest_word = ""
    
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Reemplazamos únicamente los símbolos indicados por espacios
    clean_text = re.sub(r'[\.,:;()]', ' ', text)
    
    # Dividimos por cualquier tipo de espacio en blanco (incluye saltos de línea)
    words = clean_text.split()
    
    # Buscamos la palabra más larga. 
    # Al usar >= guardamos la última ocurrencia en caso de empate.
    for word in words:
        if len(word) >= len(longest_word):
            longest_word = word

    return longest_word


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
