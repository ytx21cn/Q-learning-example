from data_types import DataTable


def init_data_table() -> DataTable:

    data_table = DataTable(width=4, height=3)

    # set reward data
    data_table.add_reward((0, 0), -0.04)
    data_table.add_reward((0, 1), -0.04)
    data_table.add_reward((0, 2), -0.04)
    data_table.add_reward((0, 3), 1.0)
    data_table.add_reward((1, 0), -0.04)
    data_table.add_reward((1, 2), -0.04)
    data_table.add_reward((1, 3), -1.0)
    data_table.add_reward((2, 0), -0.04)
    data_table.add_reward((2, 1), -0.04)
    data_table.add_reward((2, 2), -0.04)
    data_table.add_reward((2, 3), -0.04)

    # set start and terminal states
    data_table.set_start((2, 0))
    data_table.add_terminal((0, 3))
    data_table.add_terminal((1, 3))

    return data_table
