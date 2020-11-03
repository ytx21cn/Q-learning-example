from data import init_data_table
from bellman_iteration import bellman_update_utilities


def main():
    data_table = init_data_table()
    for i in range(36):
        if i > 0:
            bellman_update_utilities(data_table)
        print(f'[{i}]')
        print(data_table.utilities)


if __name__ == '__main__':
    main()
