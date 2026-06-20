# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test__enablelegacywindowsfsencoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = ('import sys', 'sys._enablelegacywindowsfsencoding()', 'print(sys.getfilesystemencoding(), sys.getfilesystemencodeerrors())')
    (rc, out, err) = assert_python_ok('-c', '; '.join(code))
    out = out.decode('ascii', 'replace').rstrip()
    self.assertEqual(out, 'mbcs replace')
