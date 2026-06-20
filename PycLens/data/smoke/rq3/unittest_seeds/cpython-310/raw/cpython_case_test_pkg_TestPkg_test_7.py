# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkg.py
# case: TestPkg_test_7

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hier = [('t7.py', ''), ('t7', None), ('t7 __init__.py', ''), ('t7 sub.py', "raise RuntimeError('Shouldnt load sub.py')"), ('t7 sub', None), ('t7 sub __init__.py', ''), ('t7 sub .py', "raise RuntimeError('Shouldnt load subsub.py')"), ('t7 sub subsub', None), ('t7 sub subsub __init__.py', 'spam = 1')]
    self.mkhier(hier)
    (t7, sub, subsub) = (None, None, None)
    import t7 as tas
    self.assertEqual(fixdir(dir(tas)), ['__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__'])
    self.assertFalse(t7)
    from t7 import sub as subpar
    self.assertEqual(fixdir(dir(subpar)), ['__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__'])
    self.assertFalse(t7)
    self.assertFalse(sub)
    from t7.sub import subsub as subsubsub
    self.assertEqual(fixdir(dir(subsubsub)), ['__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'spam'])
    self.assertFalse(t7)
    self.assertFalse(sub)
    self.assertFalse(subsub)
    from t7.sub.subsub import spam as ham
    self.assertEqual(ham, 1)
    self.assertFalse(t7)
    self.assertFalse(sub)
    self.assertFalse(subsub)
