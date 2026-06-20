# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_with_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('c:a/b').with_name('d.xml'), P('c:a/d.xml'))
    self.assertEqual(P('c:/a/b').with_name('d.xml'), P('c:/a/d.xml'))
    self.assertEqual(P('c:a/Dot ending.').with_name('d.xml'), P('c:a/d.xml'))
    self.assertEqual(P('c:/a/Dot ending.').with_name('d.xml'), P('c:/a/d.xml'))
    self.assertRaises(ValueError, P('c:').with_name, 'd.xml')
    self.assertRaises(ValueError, P('c:/').with_name, 'd.xml')
    self.assertRaises(ValueError, P('//My/Share').with_name, 'd.xml')
    self.assertRaises(ValueError, P('c:a/b').with_name, 'd:')
    self.assertRaises(ValueError, P('c:a/b').with_name, 'd:e')
    self.assertRaises(ValueError, P('c:a/b').with_name, 'd:/e')
    self.assertRaises(ValueError, P('c:a/b').with_name, '//My/Share')
