# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_resolve_dot

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE)
    self.dirlink('.', join('0'))
    self.dirlink(os.path.join('0', '0'), join('1'))
    self.dirlink(os.path.join('1', '1'), join('2'))
    q = p / '2'
    self.assertEqual(q.resolve(strict=True), p)
    r = q / '3' / '4'
    self.assertRaises(FileNotFoundError, r.resolve, strict=True)
    self.assertEqual(r.resolve(strict=False), p / '3' / '4')
