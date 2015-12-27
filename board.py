from output import Output

class Board:
    def __init__(self, letters):
        self.size = len(letters)
        self.neighbours = {}

        for row in letters:
            if len(row) != self.size:
                raise ValueError("Bad list size %s, expected %s" % (len(row), self.size))

        for x in range(self.size):
            self.neighbours[x] = []
            for y in range (self.size):
                self.neighbours[x].append(self._calc_neighbours(x, y))

        self.letters = letters

    def get_letter(self, col, row):
        if col >= self.size or row >= self.size:
            raise ValueError("Bad coordinates")

        return self.letters[row][col]

    def _calc_neighbours(self, col, row):
        neighbours = []
        for c in range(col-1, col+2):
            for r in range(row-1, row+2):
                neighbours.append((c, r))
        neighbours.remove((col,row))
        return filter(lambda t: t[0] in range(0, self.size) and t[1] in range(0, self.size), neighbours)

    def get_neighbours(self, col, row):
        return self.neighbours[col][row]

    def __str__(self):
        output = Output()

        output.thick_bar(13)
        output.add('|           |')

        for row in self.letters:
            output.add('|  ' + ' '.join(row) + '  |')

        output.add('|           |')
        output.thick_bar(13)

        return str(output)