def run(radius: float) -> float:
    # TODO
    volume = (4 / 3) * 3.14 * (radius ** 3)
    print(f"Volume of sphere with radius {radius} = {volume}")
    return volume

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
