# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_get_referents

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    alist = [1, 3, 5]
    got = gc.get_referents(alist)
    got.sort()
    self.assertEqual(got, alist)
    atuple = tuple(alist)
    got = gc.get_referents(atuple)
    got.sort()
    self.assertEqual(got, alist)
    adict = {1: 3, 5: 7}
    expected = [1, 3, 5, 7]
    got = gc.get_referents(adict)
    got.sort()
    self.assertEqual(got, expected)
    got = gc.get_referents([1, 2], {3: 4}, (0, 0, 0))
    got.sort()
    self.assertEqual(got, [0, 0] + list(range(5)))
    self.assertEqual(gc.get_referents(1, 'a', 4j), [])
