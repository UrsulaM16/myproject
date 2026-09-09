def run(word1: str, word2: str) -> str:
    # TODO
    half1 = word1[:len(word1)//2]
    half2 = word2[len(word2)//2:]
    turn = half1 + half2
    return turn


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
