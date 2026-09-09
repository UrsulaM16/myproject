def run(arc_a: float) -> float:
    # TODO
    PI: float = 3.14
    radio: float = (arc_a * 2) / PI
    area: float = radio ** 2
    return round(number=area, ndigits=10)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
