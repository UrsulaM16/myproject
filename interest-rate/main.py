def run(amount: float, rate: float, years: int) -> float:
    # TODO
    future_amount = amount * ((1 + rate/100) ** years)
    print(f"Future amount: {future_amount}")
    return future_amount


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
