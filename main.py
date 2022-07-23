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
                (1, 1),
                (5,),
                (3,),
                (4,)
            ],
        'row':
            [
                (2,),
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
        for y, instruction in enumerate(task['column']):
            offset = height - (sum(instruction) + len(instruction) - 1)
            if offset < min(instruction):
                print(f'[*] Column {task["column"].index(instruction)} is solvable')
                give_up = False
                # solving...
                if offset == 0:
                    i = 0
                    for group in instruction:
                        for pixel in range(group):
                            board[i][y] = True
                            i += 1
                        if i == height:
                            i = 0
                            break
                        board[i][y] = False
                        i += 1
                else:
                    temp_line = []
                    for group in instruction:
                        for pixel in range(group):
                            temp_line.append(group)
                        temp_line.append(0)
                    temp_line.pop()

                    temp_col_shifted = temp_line.copy()
                    for _ in range(offset):
                        temp_col_shifted.insert(0, -1)
                        temp_col_shifted.pop()

                    i = 0
                    for a, b in zip(temp_line, temp_col_shifted):
                        if a == b and a != 0:
                            board[i][y] = True
                        i += 1

        for x, instruction in enumerate(task['row']):
            offset = width - (sum(instruction) + len(instruction) - 1)
            if offset < min(instruction):
                print(f'[*] Row {task["row"].index(instruction)} is solvable')
                give_up = False
                # solving...
                if offset == 0:
                    i = 0
                    for group in instruction:
                        for pixel in range(group):
                            board[x][i] = True
                            i += 1
                        if i == height:
                            i = 0
                            break
                        board[x][i] = False
                        i += 1
                else:
                    temp_line = []
                    for group in instruction:
                        for pixel in range(group):
                            temp_line.append(group)
                        temp_line.append(0)
                    temp_line.pop()

                    temp_col_shifted = temp_line.copy()
                    for _ in range(offset):
                        temp_col_shifted.insert(0, -1)
                        temp_col_shifted.pop()

                    i = 0
                    for a, b in zip(temp_line, temp_col_shifted):
                        if a == b and a != 0:
                            board[x][i] = True
                        i += 1

        give_up = True
        if give_up is True:
            print('[:<] Gave up')
            print_board(board)
            break
        else:
            give_up = True

if __name__ == '__main__':
    main()
