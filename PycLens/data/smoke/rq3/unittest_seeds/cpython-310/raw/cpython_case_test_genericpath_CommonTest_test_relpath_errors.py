# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: CommonTest_test_relpath_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings_helper.check_warnings(('', (BytesWarning, DeprecationWarning)), quiet=True):
        errmsg = "Can't mix strings and bytes in path components"
        with self.assertRaisesRegex(TypeError, errmsg):
            self.pathmodule.relpath(b'bytes', 'str')
        with self.assertRaisesRegex(TypeError, errmsg):
            self.pathmodule.relpath('str', b'bytes')
        with self.assertRaisesRegex(TypeError, 'int'):
            self.pathmodule.relpath(42, 'str')
        with self.assertRaisesRegex(TypeError, 'int'):
            self.pathmodule.relpath('str', 42)
        with self.assertRaisesRegex(TypeError, 'bytearray'):
            self.pathmodule.relpath(bytearray(b'foo'), bytearray(b'bar'))
