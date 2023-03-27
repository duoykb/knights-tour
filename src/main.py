from src import moves, tools


def find_sequence(start):
    def helper(_moves, _visited_moves):

        if len(_visited_moves) == 64:
            raise Exception()

        for move in _moves:

            if move in _visited_moves:
                continue

            _visited_moves.append(move)
            helper(moves.find_available_moves(move), _visited_moves)
            del _visited_moves[-1]

    visited_moves = [start]
    try:
        helper(moves.find_available_moves(start), visited_moves)
    except Exception:
        pass

    return visited_moves


tools.display_board()
print(find_sequence(12))