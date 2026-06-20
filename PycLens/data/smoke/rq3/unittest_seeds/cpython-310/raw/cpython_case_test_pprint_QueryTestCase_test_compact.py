# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_compact

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = [list(range(i * i)) for i in range(5)] + [list(range(i)) for i in range(6)]
    expected = '[[], [0], [0, 1, 2, 3],\n [0, 1, 2, 3, 4, 5, 6, 7, 8],\n [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,\n  14, 15],\n [], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3],\n [0, 1, 2, 3, 4]]'
    self.assertEqual(pprint.pformat(o, width=47, compact=True), expected)
