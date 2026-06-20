# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_glob_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _check(glob, expected):
        self.assertEqual(set(glob), {P(BASE, q) for q in expected})
    P = self.cls
    p = P(BASE)
    it = p.glob('fileA')
    self.assertIsInstance(it, collections.abc.Iterator)
    _check(it, ['fileA'])
    _check(p.glob('fileB'), [])
    _check(p.glob('dir*/file*'), ['dirB/fileB', 'dirC/fileC'])
    if not os_helper.can_symlink():
        _check(p.glob('*A'), ['dirA', 'fileA'])
    else:
        _check(p.glob('*A'), ['dirA', 'fileA', 'linkA'])
    if not os_helper.can_symlink():
        _check(p.glob('*B/*'), ['dirB/fileB'])
    else:
        _check(p.glob('*B/*'), ['dirB/fileB', 'dirB/linkD', 'linkB/fileB', 'linkB/linkD'])
    if not os_helper.can_symlink():
        _check(p.glob('*/fileB'), ['dirB/fileB'])
    else:
        _check(p.glob('*/fileB'), ['dirB/fileB', 'linkB/fileB'])
