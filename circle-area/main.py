def run(radius: float) -> float:
    # TODO
    area = 3.14 * radius ** 2
    print(f"Area of circle with radius {radius} = {area}")
    return area


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
