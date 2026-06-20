# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('c:').name, '')
    self.assertEqual(P('c:/').name, '')
    self.assertEqual(P('c:a/b').name, 'b')
    self.assertEqual(P('c:/a/b').name, 'b')
    self.assertEqual(P('c:a/b.py').name, 'b.py')
    self.assertEqual(P('c:/a/b.py').name, 'b.py')
    self.assertEqual(P('//My.py/Share.php').name, '')
    self.assertEqual(P('//My.py/Share.php/a/b').name, 'b')
