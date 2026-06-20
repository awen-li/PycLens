# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_import

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    __import__('sys')
    __import__('time')
    __import__('string')
    __import__(name='sys')
    __import__(name='time', level=0)
    self.assertRaises(ModuleNotFoundError, __import__, 'spamspam')
    self.assertRaises(TypeError, __import__, 1, 2, 3, 4)
    self.assertRaises(ValueError, __import__, '')
    self.assertRaises(TypeError, __import__, 'sys', name='sys')
    with self.assertWarns(ImportWarning):
        self.assertRaises(ImportError, __import__, '', {'__package__': None, '__spec__': None, '__name__': '__main__'}, locals={}, fromlist=('foo',), level=1)
    self.assertRaises(ModuleNotFoundError, __import__, 'string\x00')
