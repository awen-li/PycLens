# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_read_skipinitialspace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._read_test(['no space, space,  spaces,\ttab'], [['no space', 'space', 'spaces', '\ttab']], skipinitialspace=True)
