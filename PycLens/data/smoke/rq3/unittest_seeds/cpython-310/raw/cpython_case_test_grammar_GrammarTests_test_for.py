# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_for

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in (1, 2, 3):
        pass
    for (i, j, k) in ():
        pass
    else:
        pass

    class Squares:

        def __init__(self, max):
            self.max = max
            self.sofar = []

        def __len__(self):
            return len(self.sofar)

        def __getitem__(self, i):
            if not 0 <= i < self.max:
                raise IndexError
            n = len(self.sofar)
            while n <= i:
                self.sofar.append(n * n)
                n = n + 1
            return self.sofar[i]
    n = 0
    for x in Squares(10):
        n = n + x
    if n != 285:
        self.fail('for over growing sequence')
    result = []
    for (x,) in [(1,), (2,), (3,)]:
        result.append(x)
    self.assertEqual(result, [1, 2, 3])
