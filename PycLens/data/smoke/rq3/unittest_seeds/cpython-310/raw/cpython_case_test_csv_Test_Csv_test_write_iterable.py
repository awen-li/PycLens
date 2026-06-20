# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_write_iterable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._write_test(iter(['a', 1, 'p,q']), 'a,1,"p,q"')
    self._write_test(iter(['a', 1, None]), 'a,1,')
    self._write_test(iter([]), '')
    self._write_test(iter([None]), '""')
    self._write_error_test(csv.Error, iter([None]), quoting=csv.QUOTE_NONE)
    self._write_test(iter([None, None]), ',')
