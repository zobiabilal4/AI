class Puzzle8:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def find_blank_tile(self, state):
        return state.index(0)

    def get_successors(self, state):
        blank_tile_index = self.find_blank_tile(state)
        successors = []
        possible_moves = [1, -1, 3, -3]  # Move right, left, down, up
        for move in possible_moves:
            if 0 <= blank_tile_index + move < 9:
                new_state = state[:]
                new_state[blank_tile_index], new_state[blank_tile_index + move] = (
                    new_state[blank_tile_index + move],
                    new_state[blank_tile_index],
                )
                successors.append(new_state)
        return successors

    def is_goal_state(self, state):
        return state == self.goal_state

    def is_solvable(self, state):
        inversion_count = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                    inversion_count += 1
        return inversion_count % 2 == 0

    def depth_limited_search(self, state, depth_limit):
        if self.is_goal_state(state):
            return [state]

        if depth_limit == 0:
            return None

        successors = self.get_successors(state)
        for successor in successors:
            result = self.depth_limited_search(successor, depth_limit - 1)
            if result is not None:
                return [state] + result

        return None

    def iterative_deepening_search(self):
        if not self.is_solvable(self.initial_state):
            return None

        depth_limit = 0
        while True:
            result = self.depth_limited_search(self.initial_state, depth_limit)
            if result is not None:
                return result
            depth_limit += 1


# Example usage
def main():
    initial_state = [1, 5, 3, 2, 7, 4, 6, 0, 8]
    puzzle_solver = Puzzle8(initial_state)
    solution = puzzle_solver.iterative_deepening_search()

    if solution:
        print("Solution found:")
        for step, state in enumerate(solution):
            print(f"Step {step}: {state}")
    else:
        print("No solution found.")
main()
