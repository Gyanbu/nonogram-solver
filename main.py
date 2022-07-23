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
    task = {}
    width = 5
    height = 5

    blank_col = []
    for col in range(width):
        task[f'c{col + 1}'] = ()
        blank_col.append(None)

    board = []
    for row in range(height):
        task[f'r{row + 1}'] = ()
        board.append(blank_col.copy())

    task = {
        'c1': (2,),
        'c2': (1,),
        'c3': (5,),
        'c4': (3,),
        'c5': (4,),

        'r1': (1,),
        'r2': (1, 1),
        'r3': (3,),
        'r4': (1, 3),
        'r5': (5,)
    }

    print(f'Instructions: {task}')

    solved = False
    while solved is not True:
        for step in task:
            step_solvable = False
            needed_space = sum(task[step]) + len(task[step]) - 1

            if step.startswith('c'):
                offset = height - needed_space
                if offset < min(task[step]):
                    print(f'[*] Step {step} is solvable')
                    step_solvable = True

            elif step.startswith('r'):
                offset = height - needed_space
                if offset < min(task[step]):
                    print(f'[*] Step {step} is solvable')
                    step_solvable = True

            if step_solvable is True:
                pass

        return


if __name__ == '__main__':
    main()
