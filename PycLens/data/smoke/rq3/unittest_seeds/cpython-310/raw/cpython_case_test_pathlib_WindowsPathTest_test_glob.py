# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: WindowsPathTest_test_glob

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P(BASE)
    self.assertEqual(set(p.glob('FILEa')), {P(BASE, 'fileA')})
    self.assertEqual(set(p.glob('F*a')), {P(BASE, 'fileA')})
    self.assertEqual(set(map(str, p.glob('FILEa'))), {f'{p}\\FILEa'})
    self.assertEqual(set(map(str, p.glob('F*a'))), {f'{p}\\fileA'})
