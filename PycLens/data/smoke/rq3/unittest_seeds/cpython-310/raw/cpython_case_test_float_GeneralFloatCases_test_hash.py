# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: GeneralFloatCases_test_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in range(-30, 30):
        self.assertEqual(hash(float(x)), hash(x))
    self.assertEqual(hash(float(sys.float_info.max)), hash(int(sys.float_info.max)))
    self.assertEqual(hash(float('inf')), sys.hash_info.inf)
    self.assertEqual(hash(float('-inf')), -sys.hash_info.inf)
