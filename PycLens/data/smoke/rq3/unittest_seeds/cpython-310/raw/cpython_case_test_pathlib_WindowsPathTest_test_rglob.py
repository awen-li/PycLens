# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: WindowsPathTest_test_rglob

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P(BASE, 'dirC')
    self.assertEqual(set(p.rglob('FILEd')), {P(BASE, 'dirC/dirD/fileD')})
    self.assertEqual(set(map(str, p.rglob('FILEd'))), {f'{p}\\dirD\\FILEd'})
