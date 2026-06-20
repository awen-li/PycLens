# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_join

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('C:/a/b')
    pp = p.joinpath('x/y')
    self.assertEqual(pp, P('C:/a/b/x/y'))
    pp = p.joinpath('/x/y')
    self.assertEqual(pp, P('C:/x/y'))
    pp = p.joinpath('D:x/y')
    self.assertEqual(pp, P('D:x/y'))
    pp = p.joinpath('D:/x/y')
    self.assertEqual(pp, P('D:/x/y'))
    pp = p.joinpath('//host/share/x/y')
    self.assertEqual(pp, P('//host/share/x/y'))
    pp = p.joinpath('c:x/y')
    self.assertEqual(pp, P('C:/a/b/x/y'))
    pp = p.joinpath('c:/x/y')
    self.assertEqual(pp, P('C:/x/y'))
