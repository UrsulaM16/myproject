def run(price_with_igic: float, igic: float) -> float:
    # TODO
    clean_price: float = price_with_igic / (1 + (igic / 100))
    return round(number=clean_price, ndigits=2)
   


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
