def run(items: list[int]) -> list[int]:
    # TODO
    LONGITUD = len(items)
    if LONGITUD > 0 :
        paso=items[LONGITUD//2] 
    return list(reversed(items[::paso] if LONGITUD > 0 else items))


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
