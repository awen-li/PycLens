# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkg.py
# case: TestPkg_test_6

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hier = [('t6', None), ('t6 __init__.py', "__all__ = ['spam', 'ham', 'eggs']"), ('t6 spam.py', ''), ('t6 ham.py', ''), ('t6 eggs.py', '')]
    self.mkhier(hier)
    import t6
    self.assertEqual(fixdir(dir(t6)), ['__all__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__'])
    s = "\n            import t6\n            from t6 import *\n            self.assertEqual(fixdir(dir(t6)),\n                             ['__all__', '__cached__', '__doc__', '__file__',\n                              '__loader__', '__name__', '__package__',\n                              '__path__', '__spec__', 'eggs', 'ham', 'spam'])\n            self.assertEqual(dir(), ['eggs', 'ham', 'self', 'spam', 't6'])\n            "
    self.run_code(s)
