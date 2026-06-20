# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_debugmallocstats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from test.support.script_helper import assert_python_ok
    args = ['-c', 'import sys; sys._debugmallocstats()']
    (ret, out, err) = assert_python_ok(*args)
    self.assertIn(b'free PyDictObjects', err)
    self.assertRaises(TypeError, sys._debugmallocstats, True)
