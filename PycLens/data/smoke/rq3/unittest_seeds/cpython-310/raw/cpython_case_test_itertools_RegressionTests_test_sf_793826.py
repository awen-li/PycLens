# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: RegressionTests_test_sf_793826

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def mutatingtuple(tuple1, f, tuple2):

        def g(value, first=[1]):
            if first:
                del first[:]
                f(next(z))
            return value
        items = list(tuple2)
        items[1:1] = list(tuple1)
        gen = map(g, items)
        z = zip(*[gen] * len(tuple1))
        next(z)

    def f(t):
        global T
        T = t
        first[:] = list(T)
    first = []
    mutatingtuple((1, 2, 3), f, (4, 5, 6))
    second = list(T)
    self.assertEqual(first, second)
