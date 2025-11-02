def player(prev_play, opponent_history=[]):
    import random

    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) == 0:
        return random.choice(["R", "P", "S"])

    last = opponent_history[-1]
    most_common = max(set(opponent_history), key=opponent_history.count)

    prediction = {"R": "P", "P": "S", "S": "R"}[most_common]

    if len(opponent_history) > 3:
        recent = opponent_history[-3:]
        if recent == ["R", "P", "S"]:
            prediction = "P"
        elif recent.count(recent[0]) == 3:
            prediction = {"R": "P", "P": "S", "S": "R"}[recent[0]]

    return prediction
