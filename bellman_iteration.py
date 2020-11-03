from copy import deepcopy
from typing import List

from data_types import DataTable, Coordinate, Direction


def __transition_sum(data_table: DataTable, coord: Coordinate,
                     trans_probs: List[float],
                     directions: List[Direction]) -> float:
    assert len(trans_probs) == len(directions)
    result = 0
    for (trans_prob, direction) in zip(trans_probs, directions):
        adj_utility = data_table.get_adjacent_utility(coord, direction)
        result += trans_prob * adj_utility
    return result


def bellman_update_utilities(data_table: DataTable) -> DataTable:

    gamma = data_table.gamma

    orig_utilities = data_table.utilities
    new_utilities = deepcopy(orig_utilities)

    # transition probabilities
    trans_prob1 = 0.8
    trans_prob2 = 0.1
    trans_prob3 = 0.1
    trans_probs = [trans_prob1, trans_prob2, trans_prob3]

    for coord, reward in data_table.rewards.items():
        if coord in data_table.terminals:
            continue

        u1 = __transition_sum(
            data_table, coord,
            trans_probs=trans_probs,
            directions=[Direction.UP, Direction.LEFT, Direction.RIGHT]
        )
        u2 = __transition_sum(
            data_table, coord,
            trans_probs=trans_probs,
            directions=[Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        )
        u3 = __transition_sum(
            data_table, coord,
            trans_probs=trans_probs,
            directions=[Direction.LEFT, Direction.UP, Direction.DOWN]
        )
        u4 = __transition_sum(
            data_table, coord,
            trans_probs=trans_probs,
            directions=[Direction.RIGHT, Direction.UP, Direction.DOWN]
        )

        new_utility = reward + gamma * max(u1, u2, u3, u4)
        new_utilities[coord] = new_utility

    data_table.utilities = new_utilities
    return data_table
