def run(year: int) -> int:
    # TODO
    century: int = (year + 99) // 100
    return century


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
