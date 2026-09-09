def run(a: int, b: int, c: int) -> tuple:
       discriminant: float = ( b ** 2 - ( 4 * a * c ) ) ** 0.5
       x1: float = (- b + discriminant) / (2 * a)
       x2: float = (- b - discriminant) / (2 * a)
       return x1, x2

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
