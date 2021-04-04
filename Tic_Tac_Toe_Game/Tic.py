def find_winner(board):
    n = len(board)
    """
    We can write length code to verify N row, N every col and 2 diagonals
    Notice: the behaviour of all of them is SAME
        E.g. We have some starting point (e.g. 0 0) and we need to verify its row
    We can use a direction-array style to write an elegant code
    We will create a single list with the 2N+2 needed verifications
    For every verification we need 4 values:
        The starting point (r, c): we need startings for N rows, N cols, 2 Diagonals
        The direction to move in it for N steps

    For example, for the starting (0, 0)
        To verify its row, we need direction (1, 0)
        To verify its col, we need direction (0, 1)
        To verify its diagonal, we need direction (1, 1)
    To verify the right diagonal: we start from the last cell in first row (0, n-1) and moves (1, -1)
        1 means move to next row. -1 means move to the previous column

    Once done: we iterate over all such start/direction. 
        Loop n times to verify they all same play symbol 
    """
    start_dir = [(r, 0, 0, 1) for r in range(n)]  # Add N row starting points/dir
    start_dir.extend([(0, c, 1, 0) for c in range(n)])  # Add N col starting points/dir
    start_dir.append((0, 0, 1, 1))  # Add left diagonal
    start_dir.append((0, n - 1, 1, -1))  # Add right diagonal

    for r, c, dr, dc in start_dir:
        player = board[r][c]
        if player == ' ':
            continue
        is_win = True
        for s in range(n):
            if board[r][c] != player:
                is_win = False
                break
            r, c = r + dr, c + dc  # move to next position
        if is_win:
            return player
    return None


if __name__ == '__main__':
    n = int(input('Enter grid size: '))
    assert n >= 3
    board = [[' '] * n for i in range(n)]
    symbols = 'XO'
    steps, turn = 0, 0

    while True:
        if steps == n * n:
            print('Tie!')
            break
        r, c = map(int, input(f'Player {symbols[turn]}, make a move: ').split())
        r, c = r - 1, c - 1
        if not 0 <= r < n or not 0 <= c < n or board[r][c] != ' ':
            print('Invalid location. Try again')
            continue
        board[r][c] = symbols[turn]
        print('\n'.join(['|'.join(row) for row in board]))

        if (winner := find_winner(board)) is not None:  # without parentheses, walrus is assigned boolean!
            print(f'Play {winner} won!')
            break
        turn = 1 - turn  # switch 0 to 1 and 1 to 0
        steps += 1

"""
3
1 1
1 2
2 2
1 3
3 3
X|O|O
 |X| 
 | |X
Play X won!

3
1 1
1 2
2 1
2 2
3 3
3 2
X|O| 
X|O| 
 |O|X
Play O won!

3
1 3
1 1
2 2
3 3
3 1
O| |X
 |X| 
X| |O
Play X won!

3
1 1
1 3
1 2
2 2
3 2
2 1
2 3
3 3
3 1
X|X|O
O|O|X
X|X|O
Tie!
"""