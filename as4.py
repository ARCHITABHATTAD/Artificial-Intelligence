class NQueens:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def is_safe(self, queens, row, col):
        for r, c in queens:
            if row == r or col == c or abs(row - r) == abs(col - c):
                return False
        return True

    def backtrack(self, queens):
        if len(queens) == self.n:
            self.solutions.append(queens)
            return

        for col in range(self.n):
            if self.is_safe(queens, len(queens), col):
                self.backtrack(queens + [(len(queens), col)])

    def solve(self):
        self.backtrack([])
        return self.solutions


n = int(input("Enter the number of queens: "))
queens = NQueens(n)
solutions = queens.solve()

if solutions:
    print(f"Found {len(solutions)} solution(s) for the {n}-queens problem:")
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row, col in solution:
            print(f"Queen at row {row} and column {col}")
        print()
else:
    print(f"No solution found for the {n}-queens problem.")
