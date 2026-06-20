# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: EnvironTests_test_keyvalue_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (key, val) in os.environ.items():
        self.assertEqual(type(key), str)
        self.assertEqual(type(val), str)
