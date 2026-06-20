# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_write_bigfield

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bigstring = 'X' * 50000
    self._write_test([bigstring, bigstring], '%s,%s' % (bigstring, bigstring))
