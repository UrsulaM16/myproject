def run(A: list, B: list) -> list:
    return [
        [A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)]
        for i in range(2)
    ]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

