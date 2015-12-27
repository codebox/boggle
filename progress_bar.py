import sys

class ProgressBar:
    def __init__(self, l):
        self.l = l
        self.value = 0
        self.previous = None

    def _build_text(self, v):
        return '[' + (v * '#') + ((self.l-v) * '.') + ']'

    def show(self, new_value):
        output = ''
        if self.previous != None:
            output += '\b' * (len(self._build_text(self.previous)) + 1)
        output += self._build_text(new_value)
        print output,
        sys.stdout.flush()

        self.previous = self.value
        self.value = new_value

    def finish(self):
        self.show(self.l)
        print ''