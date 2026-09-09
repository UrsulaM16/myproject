def run(year: int) -> bool:
    # TODO
    if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        is_leap_year = True
    else:
        is_leap_year = False
    return is_leap_year


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
