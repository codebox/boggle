BAR_LENGTH = 40

class Output:
    def __init__(self):
        self.lines = []

    def add(self, line):
        self.lines.append(line)

    def blank_line(self):
        self.lines.append('')

    def thin_bar(self, length=BAR_LENGTH):
        self.lines.append('-' * length)

    def thick_bar(self, length=BAR_LENGTH):
        self.lines.append('=' * length)

    def __str__(self):
        return '\n'.join(self.lines)
