def run(speed_km_h: float) -> float:
    # TODO
    km_h_to_cm_s: float = 100000 / 3600
    speed_cm_s: float = float(int(speed_km_h * km_h_to_cm_s))
    return speed_cm_s


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
