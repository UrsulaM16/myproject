def run(values: list) -> int:
    # TODO
    minimo = values[0]
    for n in values:
        if n < minimo:
            minimo = int(n)
    return minimo


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
