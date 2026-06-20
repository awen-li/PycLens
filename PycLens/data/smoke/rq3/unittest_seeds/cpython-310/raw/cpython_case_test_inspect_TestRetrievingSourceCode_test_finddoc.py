# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestRetrievingSourceCode_test_finddoc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    finddoc = inspect._finddoc
    self.assertEqual(finddoc(int), int.__doc__)
    self.assertEqual(finddoc(int.to_bytes), int.to_bytes.__doc__)
    self.assertEqual(finddoc(int().to_bytes), int.to_bytes.__doc__)
    self.assertEqual(finddoc(int.from_bytes), int.from_bytes.__doc__)
    self.assertEqual(finddoc(int.real), int.real.__doc__)
