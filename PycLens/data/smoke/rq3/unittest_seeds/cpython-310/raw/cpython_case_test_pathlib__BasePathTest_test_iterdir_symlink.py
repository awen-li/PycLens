# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_iterdir_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P(BASE, 'linkB')
    paths = set(p.iterdir())
    expected = {P(BASE, 'linkB', q) for q in ['fileB', 'linkD']}
    self.assertEqual(paths, expected)
