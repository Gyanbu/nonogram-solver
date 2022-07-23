def print_board(board):
    print()
    for col in board:
        for pixel in col:
            if pixel is None:
                print('-', end=' ')
            elif pixel is False:
                print('X', end=' ')
            elif pixel is True:
                print('O', end=' ')
            else:
                print('[!] Error!')
                print(f'[!] Item in board is {pixel}')
        print()


def main():
    task = {
        'column': [],
        'row': []
    }
    width = 5
    height = 5

    blank_col = []
    for col in range(width):
        task['column'].append(())
        blank_col.append(None)

    board = []
    for row in range(height):
        task['row'].append(())
        board.append(blank_col.copy())

    task = {
        'column':
            [
                (2,),
                (1,),
                (5,),
                (3,),
                (4,)
            ],
        'row':
            [
                (1,),
                (1, 1),
                (3,),
                (1, 3),
                (5,)
            ]
    }

    print(board)
    print(f'Instructions: {task}')


    give_up = True
    while True:

        for x, instruction in enumerate(task['column']):
            offset = height - (sum(instruction) + len(instruction) - 1)
            if offset < min(instruction):
                print(f'[*] Column {task["column"].index(instruction)} is solvable')
                give_up = False
                # solving...
                for pixel in board[x]:
                    pass

        for instruction in task['row']:
            offset = width - (sum(instruction) + len(instruction) - 1)
            if offset < min(instruction):
                print(f'[*] Column {task["row"].index(instruction)} is solvable')
                give_up = False
                # solving...

        give_up = True
        if give_up is True:
            print('[:<] Gave up')
            print_board(board)
            break
        else:
            give_up = True


if __name__ == '__main__':
    main()
