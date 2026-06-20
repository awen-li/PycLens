# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorPickleTestCase_test_itemgetter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    itemgetter = self.module.itemgetter
    a = 'ABCDE'
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.subTest(proto=proto):
            f = itemgetter(2)
            f2 = self.copy(f, proto)
            self.assertEqual(repr(f2), repr(f))
            self.assertEqual(f2(a), f(a))
            f = itemgetter(2, 0, 4)
            f2 = self.copy(f, proto)
            self.assertEqual(repr(f2), repr(f))
            self.assertEqual(f2(a), f(a))
