# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_compile_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for filename in ('file.py', b'file.py'):
        code = compile('pass', filename, 'exec')
        self.assertEqual(code.co_filename, 'file.py')
    for filename in (bytearray(b'file.py'), memoryview(b'file.py')):
        with self.assertWarns(DeprecationWarning):
            code = compile('pass', filename, 'exec')
        self.assertEqual(code.co_filename, 'file.py')
    self.assertRaises(TypeError, compile, 'pass', list(b'file.py'), 'exec')
