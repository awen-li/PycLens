# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkg.py
# case: TestPkg_test_4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hier = [('t4.py', "raise RuntimeError('Shouldnt load t4.py')"), ('t4', None), ('t4 __init__.py', ''), ('t4 sub.py', "raise RuntimeError('Shouldnt load sub.py')"), ('t4 sub', None), ('t4 sub __init__.py', ''), ('t4 sub subsub.py', "raise RuntimeError('Shouldnt load subsub.py')"), ('t4 sub subsub', None), ('t4 sub subsub __init__.py', 'spam = 1')]
    self.mkhier(hier)
    s = '\n            from t4.sub.subsub import *\n            self.assertEqual(spam, 1)\n            '
    self.run_code(s)
