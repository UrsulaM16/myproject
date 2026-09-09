def run(z: float) -> float:
    # TODO
    PI = 3.14
    r_interior = z / 2
    r_exterior = z + r_interior
    area_total = PI * (r_exterior**2)
    area_interior = PI * (r_interior**2)
    gray_area = area_total - area_interior
    return gray_area


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)