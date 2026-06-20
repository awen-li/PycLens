# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectRegistry_test_bad_dialect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, csv.reader, [], bad_attr=0)
    self.assertRaises(TypeError, csv.reader, [], delimiter=None)
    self.assertRaises(TypeError, csv.reader, [], quoting=-1)
    self.assertRaises(TypeError, csv.reader, [], quoting=100)
