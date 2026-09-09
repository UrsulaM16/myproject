def run(player1: str, player2: str) -> int:
    # TODO
    p1 = player1.lower()
    p2 = player2.lower()
    if p1 == p2:
        winner = 0
    elif (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
        winner = 1
    else:
        winner = 2
    return winner


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
