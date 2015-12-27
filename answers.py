from output import Output

class Answers:
    points = {
        3 : 1,
        4 : 1,
        5 : 2,
        6 : 3,
        7 : 5,
        8 : 11
    }

    def __init__(self):
        self.words = set()

    def add(self, words):
        self.words.update(words)

    def _make_dict(self):
        words_by_length = {}

        for word in sorted(self.words):
            l = len(word)

            if not words_by_length.has_key(l):
                words_by_length[l] = []

            words_by_length[l].append(word)

        return words_by_length

    def _calc_points(self):
        total = 0

        for word in self.words:
            total += self.points[min(len(word), 8)]

        return total

    def __str__(self):
        output = Output()

        output.thick_bar()
        output.add('Found {} words ({} points available)'.format(len(self.words), self._calc_points()))

        words_by_length = self._make_dict()
        for length in words_by_length:
            output.thin_bar()
            output.add('{}: {}'.format(length, ' '.join(words_by_length[length])))

        output.thick_bar()

        return str(output)