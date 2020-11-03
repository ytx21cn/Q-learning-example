from types import DataTable

# set reward data
data_table = DataTable(width=4, height=3)
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
