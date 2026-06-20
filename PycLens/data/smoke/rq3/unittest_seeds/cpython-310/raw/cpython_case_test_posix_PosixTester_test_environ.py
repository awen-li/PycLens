# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_environ

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if os.name == 'nt':
        item_type = str
    else:
        item_type = bytes
    for (k, v) in posix.environ.items():
        self.assertEqual(type(k), item_type)
        self.assertEqual(type(v), item_type)
