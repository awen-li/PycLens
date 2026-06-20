# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: MiscTests_test_getcwdb

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cwd = os.getcwdb()
    self.assertIsInstance(cwd, bytes)
    self.assertEqual(os.fsdecode(cwd), os.getcwd())
