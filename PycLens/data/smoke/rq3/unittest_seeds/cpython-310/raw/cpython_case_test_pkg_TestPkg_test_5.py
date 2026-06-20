# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkg.py
# case: TestPkg_test_5

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hier = [('t5', None), ('t5 __init__.py', 'import t5.foo'), ('t5 string.py', 'spam = 1'), ('t5 foo.py', 'from . import string; assert string.spam == 1')]
    self.mkhier(hier)
    import t5
    s = "\n            from t5 import *\n            self.assertEqual(dir(), ['foo', 'self', 'string', 't5'])\n            "
    self.run_code(s)
    import t5
    self.assertEqual(fixdir(dir(t5)), ['__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'foo', 'string', 't5'])
    self.assertEqual(fixdir(dir(t5.foo)), ['__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'string'])
    self.assertEqual(fixdir(dir(t5.string)), ['__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'spam'])
