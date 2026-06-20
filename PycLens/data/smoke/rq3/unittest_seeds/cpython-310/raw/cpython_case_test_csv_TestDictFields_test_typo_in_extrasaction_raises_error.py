# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDictFields_test_typo_in_extrasaction_raises_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fileobj = StringIO()
    self.assertRaises(ValueError, csv.DictWriter, fileobj, ['f1', 'f2'], extrasaction='raised')
