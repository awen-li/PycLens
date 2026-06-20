# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iterlen.py
# case: TestListReversed_test_mutation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = list(range(n))
    it = reversed(d)
    next(it)
    next(it)
    self.assertEqual(length_hint(it), n - 2)
    d.append(n)
    self.assertEqual(length_hint(it), n - 2)
    d[1:] = []
    self.assertEqual(length_hint(it), 0)
    self.assertEqual(list(it), [])
    d.extend(range(20))
    self.assertEqual(length_hint(it), 0)
