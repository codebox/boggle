import random

class Cubes:
    CUBES = map(list, [
        'IBALTY',
        'BAJOQM',
        'GLYUEK',
        'PUETLS',
        'PCMDAE',
        'COATIA',
        'UNOTDK',
        'DWSNEO',
        'WRLGIU',
        'CLARES',
        'FIOBRX',
        'DAZNEV',
        'GETINV',
        'PIESHN',
        'FEYHIE',
        'SHRMAO'
    ])

    def _make_row(self, l):
        return map(lambda t : random.choice(t), l)

    def shuffle(self):
        return [
            self._make_row(Cubes.CUBES[0:4]),
            self._make_row(Cubes.CUBES[4:8]),
            self._make_row(Cubes.CUBES[8:12]),
            self._make_row(Cubes.CUBES[12:16])]