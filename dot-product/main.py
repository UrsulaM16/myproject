def run(u: list, v: list) -> float | None:
    # TODO
  

    if len(u) != len(v):
        return None

    dprod = 0

    for x, y in zip(u, v):
        dprod += x * y
    

    return dprod


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
