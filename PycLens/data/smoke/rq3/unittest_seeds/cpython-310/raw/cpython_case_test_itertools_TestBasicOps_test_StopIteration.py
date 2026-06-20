# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_StopIteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(StopIteration, next, zip())
    for f in (chain, cycle, zip, groupby):
        self.assertRaises(StopIteration, next, f([]))
        self.assertRaises(StopIteration, next, f(StopNow()))
    self.assertRaises(StopIteration, next, islice([], None))
    self.assertRaises(StopIteration, next, islice(StopNow(), None))
    (p, q) = tee([])
    self.assertRaises(StopIteration, next, p)
    self.assertRaises(StopIteration, next, q)
    (p, q) = tee(StopNow())
    self.assertRaises(StopIteration, next, p)
    self.assertRaises(StopIteration, next, q)
    self.assertRaises(StopIteration, next, repeat(None, 0))
    for f in (filter, filterfalse, map, takewhile, dropwhile, starmap):
        self.assertRaises(StopIteration, next, f(lambda x: x, []))
        self.assertRaises(StopIteration, next, f(lambda x: x, StopNow()))
