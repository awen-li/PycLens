# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_rename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    p = P / 'fileA'
    size = p.stat().st_size
    q = P / 'dirA' / 'fileAA'
    renamed_p = p.rename(q)
    self.assertEqual(renamed_p, q)
    self.assertEqual(q.stat().st_size, size)
    self.assertFileNotFound(p.stat)
    r = rel_join('fileAAA')
    renamed_q = q.rename(r)
    self.assertEqual(renamed_q, self.cls(r))
    self.assertEqual(os.stat(r).st_size, size)
    self.assertFileNotFound(q.stat)
