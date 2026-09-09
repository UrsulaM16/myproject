def run(posicion_actual: int, dado: int) -> int:
    # TODO
    final_posicion = posicion_actual + (dado * 2)
    return final_posicion



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
