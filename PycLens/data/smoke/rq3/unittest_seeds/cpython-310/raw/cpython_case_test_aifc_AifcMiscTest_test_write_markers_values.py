# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AifcMiscTest_test_write_markers_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fout = aifc.open(io.BytesIO(), 'wb')
    self.assertEqual(fout.getmarkers(), None)
    fout.setmark(1, 0, b'foo1')
    fout.setmark(1, 1, b'foo2')
    self.assertEqual(fout.getmark(1), (1, 1, b'foo2'))
    self.assertEqual(fout.getmarkers(), [(1, 1, b'foo2')])
    fout.initfp(None)
