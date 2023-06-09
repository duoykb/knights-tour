from src import moves, tools


def prioritize(move):
    return sorted(list(moves.find_available_moves(move)), key=lambda x: len(list(moves.find_available_moves(x))))


def find_sequence(start):
    def helper(_moves, _visited_moves):

        if len(_visited_moves) == 64:
            raise Exception()

        for move in _moves:

            if move in _visited_moves:
                continue

            _visited_moves.append(move)
            helper(prioritize(move), _visited_moves)
            del _visited_moves[-1]

    visited_moves = [start]
    try:
        helper(prioritize(start), visited_moves)
    except Exception:
        pass

    return visited_moves


tools.display_board()
print(len(find_sequence(12)))
