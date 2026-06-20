# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: HamtTest_test_hashkey_helper_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    k1 = HashKey(10, 'aaa')
    k2 = HashKey(10, 'bbb')
    self.assertNotEqual(k1, k2)
    self.assertEqual(hash(k1), hash(k2))
    d = dict()
    d[k1] = 'a'
    d[k2] = 'b'
    self.assertEqual(d[k1], 'a')
    self.assertEqual(d[k2], 'b')
