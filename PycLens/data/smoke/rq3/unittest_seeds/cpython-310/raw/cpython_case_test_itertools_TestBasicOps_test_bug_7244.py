# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_bug_7244

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Repeater:

        def __init__(self, o, t, e):
            self.o = o
            self.t = int(t)
            self.e = e

        def __iter__(self):
            return self

        def __next__(self):
            if self.t > 0:
                self.t -= 1
                return self.o
            else:
                raise self.e
    r1 = Repeater(1, 3, StopIteration)
    r2 = Repeater(2, 4, StopIteration)

    def run(r1, r2):
        result = []
        for (i, j) in zip_longest(r1, r2, fillvalue=0):
            with support.captured_output('stdout'):
                print((i, j))
            result.append((i, j))
        return result
    self.assertEqual(run(r1, r2), [(1, 2), (1, 2), (1, 2), (0, 2)])
    r1 = Repeater(1, 3, RuntimeError)
    r2 = Repeater(2, 4, StopIteration)
    it = zip_longest(r1, r2, fillvalue=0)
    self.assertEqual(next(it), (1, 2))
    self.assertEqual(next(it), (1, 2))
    self.assertEqual(next(it), (1, 2))
    self.assertRaises(RuntimeError, next, it)
