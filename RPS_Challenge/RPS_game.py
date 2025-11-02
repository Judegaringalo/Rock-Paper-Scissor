import random

def play(player1, player2, num_games, verbose=False):
    player1_prev_play = ""
    player2_prev_play = ""
    player1_history = []
    player2_history = []

    for i in range(num_games):
        player1_play = player1(player2_prev_play)
        player2_play = player2(player1_prev_play)

        player1_history.append(player1_play)
        player2_history.append(player2_play)

        player1_prev_play = player1_play
        player2_prev_play = player2_play

        if verbose:
            print(f"Game {i+1}: Player1: {player1_play}, Player2: {player2_play}")

    player1_wins = sum(winner(p1, p2) == 1 for p1, p2 in zip(player1_history, player2_history))
    player2_wins = sum(winner(p1, p2) == 2 for p1, p2 in zip(player1_history, player2_history))

    print(f"Player1 wins: {player1_wins} / {num_games}")
    print(f"Player2 wins: {player2_wins} / {num_games}")

def winner(player, opponent):
    if player == opponent:
        return 0
    elif (player == "R" and opponent == "S") or (player == "S" and opponent == "P") or (player == "P" and opponent == "R"):
        return 1
    else:
        return 2

def quincy(prev_play):
    plays = ["R", "P", "S"]
    return plays[random.randint(0, 2)]

def abbey(prev_play):
    if prev_play == "":
        return "P"
    if prev_play == "R":
        return "P"
    if prev_play == "P":
        return "S"
    return "R"

def kris(prev_play):
    if prev_play == "":
        return "S"
    return prev_play

def mrugesh(prev_play):
    if prev_play == "":
        return "R"
    return {"R": "P", "P": "S", "S": "R"}[prev_play]
