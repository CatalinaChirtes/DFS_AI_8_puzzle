class PuzzleState:
    def __init__(self, board, parent, move):
        self.board = board
        self.parent = parent
        self.move = move
        self.blank = self.find_blank()

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def possible_moves(self):
        i, j = self.blank
        moves = []
        if i > 0:
            moves.append("UP")
        if i < 2:
            moves.append("DOWN")
        if j > 0:
            moves.append("LEFT")
        if j < 2:
            moves.append("RIGHT")
        return moves

    def make_move(self, move):
        i, j = self.blank
        new_board = [list(row) for row in self.board]
        if move == "UP":
            new_board[i][j], new_board[i - 1][j] = new_board[i - 1][j], new_board[i][j]
        elif move == "DOWN":
            new_board[i][j], new_board[i + 1][j] = new_board[i + 1][j], new_board[i][j]
        elif move == "LEFT":
            new_board[i][j], new_board[i][j - 1] = new_board[i][j - 1], new_board[i][j]
        elif move == "RIGHT":
            new_board[i][j], new_board[i][j + 1] = new_board[i][j + 1], new_board[i][j]
        return PuzzleState(new_board, self, move)


def display_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()


def DFS(initial_state, goal_state):
    stack = [(initial_state, [])]
    visited = set()

    while stack:
        current_state, path = stack.pop()

        if current_state == goal_state:
            return path

        visited.add(current_state)

        for move in current_state.possible_moves():
            new_state = current_state.make_move(move)
            if new_state not in visited:
                stack.append((new_state, path + [move]))

    return None


initial_board = [
    [0, 1, 3],
    [4, 2, 5],
    [7, 8, 6]
]

goal_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

initial_state = PuzzleState(initial_board, None, None)
goal_state = PuzzleState(goal_board, None, None)
print("This is the initial state:")
display_board(initial_state.board)

if initial_state == goal_state:
    print("The puzzle is already solved.")
    display_board(initial_state.board)
else:
    solution_path = DFS(initial_state, goal_state)
    if solution_path:
        print("The goal state for the 8-puzzle was found following these steps:")
        current_state = initial_state
        for step, move in enumerate(solution_path, start=1):
            print(f"Step {step}: MOVE {move}")
            current_state = current_state.make_move(move)
            display_board(current_state.board)
    else:
        print("No solution found for this 8-puzzle.")
