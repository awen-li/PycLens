# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: GetRandomTests_test_getrandom0

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    empty = os.getrandom(0)
    self.assertEqual(empty, b'')
