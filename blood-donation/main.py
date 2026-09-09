def run(age: int, weight: int, heartbeat: int, platelets: int) -> bool:
    # TODO
    
    return True if (18 <= age <= 65) and (weight > 50) and (50 <= heartbeat <= 110) and(platelets > 150000) else False


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
