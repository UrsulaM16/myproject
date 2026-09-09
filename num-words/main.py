def run(text: str) -> int:
    # TODO
    lista_palabras = text.split()
    num_words = len(lista_palabras)
    return num_words


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
