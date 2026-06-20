# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_replace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    p = P / 'fileA'
    size = p.stat().st_size
    q = P / 'dirA' / 'fileAA'
    replaced_p = p.replace(q)
    self.assertEqual(replaced_p, q)
    self.assertEqual(q.stat().st_size, size)
    self.assertFileNotFound(p.stat)
    r = rel_join('dirB', 'fileB')
    replaced_q = q.replace(r)
    self.assertEqual(replaced_q, self.cls(r))
    self.assertEqual(os.stat(r).st_size, size)
    self.assertFileNotFound(q.stat)
