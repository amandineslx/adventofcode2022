INPUT_FILE = "rock_paper_scissors-input.txt"
MOVES = {"A": "ROCK", "B": "PAPER", "C": "SCISSORS", "X": "ROCK", "Y": "PAPER", "Z": "SCISSORS"}
MOVE_PROPERTIES = {
    "ROCK": {
        "score": 1,
        "winning_move": "PAPER",
        "losing_move": "SCISSORS"
    },
    "PAPER": {
        "score": 2,
        "winning_move": "SCISSORS",
        "losing_move": "ROCK"
    },
    "SCISSORS": {
        "score": 3,
        "winning_move": "ROCK",
        "losing_move": "PAPER"
    }
}

class Round:
    def __init__(self, opponent_move, my_move):
        self.opponent_move = opponent_move
        self.my_move = my_move

def get_move_name(letter):
    return MOVES[letter]

def choose_move(opponent_move, round_outcome):
    if round_outcome == 'X':
        return MOVE_PROPERTIES[opponent_move]['losing_move']
    elif round_outcome == 'Y':
        return opponent_move
    else:
        return MOVE_PROPERTIES[opponent_move]['winning_move']

def get_round_moves(round_line):
    move_letters = round_line.split()
    moves = list(map(get_move_name, move_letters))
    round = Round(moves[0], moves[1])
    return round

def get_round_moves_from_outcome(round_line):
    letters = round_line.split()
    opponent_move = get_move_name(letters[0])
    my_move = choose_move(opponent_move, letters[1])
    print(f"Round moves: opponent-{opponent_move} mine-{my_move}")
    round = Round(opponent_move, my_move)
    return round

def get_my_round_score(round):
    score = MOVE_PROPERTIES[round.my_move]['score']
    winner = get_winner(round.opponent_move, round.my_move)
    if winner == 0:
        score = score + 3
    elif winner == 1:
        score = score + 6
    return score

def get_winner(opponent_move, my_move):
    if opponent_move == my_move:
        return 0
    elif opponent_move == MOVE_PROPERTIES[my_move]['winning_move']:
        return -1
    else:
        return 1

def get_my_score_tournament(read_line_method):
    score = 0
    with open(INPUT_FILE) as f:
        for line in f.readlines():
            print(f"Round: {line}")
            moves = read_line_method(line)
            score = score + get_my_round_score(moves)
            print(f"Score: {score}")
    return score

# print(get_my_score_tournament(get_round_moves))
print(get_my_score_tournament(get_round_moves_from_outcome))
