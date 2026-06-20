# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_dash_c_loader

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_ok('-c', 'print(__loader__)')
    expected = repr(importlib.machinery.BuiltinImporter).encode('utf-8')
    self.assertIn(expected, out)
