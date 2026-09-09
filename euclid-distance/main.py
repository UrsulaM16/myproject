def run(x1: float, y1: float, x2: float, y2: float) -> float:
    # TODO
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print(f"Distance between ({x1}, {y1}) and ({x2}, {y2}) = {distance}")
    return distance


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
