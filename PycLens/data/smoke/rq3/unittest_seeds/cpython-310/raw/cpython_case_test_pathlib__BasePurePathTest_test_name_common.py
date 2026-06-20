# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_name_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('').name, '')
    self.assertEqual(P('.').name, '')
    self.assertEqual(P('/').name, '')
    self.assertEqual(P('a/b').name, 'b')
    self.assertEqual(P('/a/b').name, 'b')
    self.assertEqual(P('/a/b/.').name, 'b')
    self.assertEqual(P('a/b.py').name, 'b.py')
    self.assertEqual(P('/a/b.py').name, 'b.py')
